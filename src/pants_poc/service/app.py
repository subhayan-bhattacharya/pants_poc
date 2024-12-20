"""Module for the service configuration."""

import contextlib
import logging

from elevait_logging import handlers
from elevait_logging.handlers import service
import fastapi
import uvicorn

import pants_poc

from . import config

_LOGGER = logging.getLogger(pants_poc.__name__)
CONFIG = config.ServiceConfig()  # type: ignore


def _configure_logging(
    logging_level: int,
    log_to_file: bool,
    slack_config: handlers.SlackConfig | None = None,
) -> None:
    """Configure the logging for the service."""
    _LOGGER.setLevel(logging_level)
    logging_handlers = [service.create_colored_stream_handler(level=logging_level)]
    if log_to_file:
        logging_handlers.append(
            service.create_rotating_file_handler(level=logging_level)
        )
    if slack_config is not None:
        logging_handlers.append(service.create_slack_handler(slack_config))
    for handler in logging_handlers:
        _LOGGER.addHandler(handler)


@contextlib.asynccontextmanager
async def _lifespan(_: fastapi.FastAPI):
    """Define what happens before and after service start."""
    _configure_logging(
        CONFIG.base_config.logging_level,
        CONFIG.base_config.log_to_file,
        CONFIG.base_config.slack_config,
    )
    yield


APP = fastapi.FastAPI(
    title=CONFIG.base_config.title,
    version=CONFIG.base_config.version,
    description=CONFIG.base_config.description,
    contact={
        "name": pants_poc.__author__,
        "email": pants_poc.__email__,
    },
    lifespan=_lifespan,
    middleware=[service.get_starlette_middleware()],
)


@APP.head("/health")
@APP.get("/health")
def health() -> None:
    """Check if the service is healthy."""
    return


@APP.get("/info")
def info() -> config.ServiceConfig:
    """Get the service configuration."""
    return CONFIG


def start_service() -> None:
    """Run the service."""
    uvicorn.run(APP, host=CONFIG.base_config.host, port=CONFIG.base_config.port)

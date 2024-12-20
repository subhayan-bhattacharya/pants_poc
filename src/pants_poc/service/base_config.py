"""The basic configuration of the service."""

# This file should not be touched.

from elevait_logging import handlers
import pydantic

import pants_poc
from pants_poc import version


class BaseConfig(pydantic.BaseModel):
    """
    Basic configuration of the service.

    Attributes
    ----------
    host
        The address where the service should be hosted.
    port
        The port where the service should run.
    title
        The title of the service.
    version
        The version of the service.
    description
        The description of the service.
    logging_level
        The logging level that should be used globally.
    log_to_file
        Whether logs should be save to a file or not.
    slack_config
        The configuration to send logs to slack.
    """

    host: str
    port: int
    title: str = pants_poc.__name__
    version: str = version.__version__
    description: str = pants_poc.__doc__
    logging_level: int
    log_to_file: bool
    slack_config: handlers.SlackConfig | None = None

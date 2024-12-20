"""Service configuration code."""

import pydantic_settings

from . import base_config


class ServiceConfig(pydantic_settings.BaseSettings):
    """Service configuration for invoice extraction."""

    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__"
    )

    base_config: base_config.BaseConfig

"""Configuration of the test suite."""

import importlib
import os
import pathlib
from typing import Generator

from fastapi import testclient
import pydantic
import pytest


@pytest.fixture(autouse=True)
def clean_environment(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Clean the environment to avoid using local environment."""
    monkeypatch.chdir(tmp_path)
    for env in os.environ:
        monkeypatch.delenv(env)


@pytest.fixture()
def set_default_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Set the environment variables."""
    monkeypatch.setenv("BASE_CONFIG__HOST", "0.0.0.0")
    monkeypatch.setenv("BASE_CONFIG__PORT", "8000")
    monkeypatch.setenv("BASE_CONFIG__LOGGING_LEVEL", "10")
    monkeypatch.setenv("BASE_CONFIG__LOG_TO_FILE", "False")


@pytest.fixture()
def client() -> Generator[testclient.TestClient, None, None]:
    """Create a test client."""
    try:
        from pants_poc.service import app

        # This is important as it resets the config, logging etc for each test in
        # case it was altered.
        app = importlib.reload(app)
    except pydantic.ValidationError as error:
        raise EnvironmentError(
            "You need to set all environment variables needed for the service."
        ) from error

    with testclient.TestClient(app.APP) as client:
        yield client

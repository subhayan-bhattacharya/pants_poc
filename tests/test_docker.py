"""Test suite for building the docker images."""

import pathlib
import socket

import pytest
from pytest_docker import plugin
import requests

_SUCCESS = 200


def _get_available_port() -> str:
    """Let the os decide what port to use."""
    sock = socket.socket()
    sock.bind(("", 0))
    return str(sock.getsockname()[1])


_PORT = _get_available_port()
pytest.MonkeyPatch().setenv("BASE_CONFIG__PORT", _PORT)


def is_responsive(url) -> bool:
    """Check if a service is available."""
    try:
        response = requests.get(url)
        return response.status_code == _SUCCESS
    except (ConnectionError, requests.ConnectionError):
        return False


@pytest.fixture(scope="session")
def docker_compose_file() -> pathlib.Path:
    """Set the path to the docker compose file."""
    return pathlib.Path(__file__).parent.parent / "docker-compose.yaml"


@pytest.fixture(scope="session")
def container_address(docker_ip: str, docker_services: plugin.Services) -> str:
    """Run the docker image."""
    port = docker_services.port_for("pants_poc", int(_PORT))
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url + "/docs")
    )
    return url


def test_info(container_address: str) -> None:
    """Check if the info endpoint is working."""
    info_endpoint = container_address + "/info"
    response = requests.get(info_endpoint)
    assert response.status_code == _SUCCESS

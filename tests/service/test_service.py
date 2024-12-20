"""Test suite for service tests."""

from fastapi import testclient
import pytest


class TestEndpoints:
    """Test endpoint related calls."""

    @pytest.mark.usefixtures("set_default_environment")
    def test_info(self, client: testclient.TestClient) -> None:
        """Test that the info endpoint is available."""
        response = client.get("/info")
        assert response.is_success

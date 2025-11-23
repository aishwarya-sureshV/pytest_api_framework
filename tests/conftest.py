# Pytest configuration file - this sets up things that all tests can use
import pytest
from http_client.client import HttpClient
from tests.helpers.api import constants


# API Client Fixtures - these create clients that tests can use

@pytest.fixture
def http_client():
    # Creates a fresh HTTP client for each test
    # This is the main client from http_client package
    return HttpClient()


@pytest.fixture
def http_client_with_base_url():
    # Creates an HTTP client with the reqres.in base URL already set
    return HttpClient(base_uri=constants.BASE_URL)


# Test Data Fixtures - these provide sample data for tests

@pytest.fixture
def sample_user_data():
    # Sample data for creating a user in tests
    return {
        "name": "Test User",
        "job": "Software Tester"
    }


@pytest.fixture
def sample_user_update_data():
    # Sample data for updating a user in tests
    return {
        "name": "Updated User",
        "job": "Senior Tester"
    }


# Pytest Configuration - registers custom markers

def pytest_configure(config):
    # This tells pytest about our custom markers
    # You can run tests with: pytest -m smoke
    config.addinivalue_line(
        "markers", "smoke: Quick smoke tests that verify basic functionality"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests that require external API"
    )


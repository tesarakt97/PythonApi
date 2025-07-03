import pytest


@pytest.fixture(scope="session")
def auth_token():
    return "Bearer test-token"  # можно читать из .env
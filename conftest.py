import pytest


@pytest.fixture(scope="session")
def auth_token():
    return "Bearer test-token"  # можно читать из .env

def pytest_addoption(parser):
    parser.addoption(
        "--alluredir=../allure-results",
        action="store",
        default="dev",
        help="Environment to run tests against: dev / qa / prod"
    )
import allure

from steps.post_steps import create_post
from utils.logger import logger

@allure.title("Create Post Test")
@allure.description("This test creates a new post and validates the response.")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_post():
    logger.info("Starting test: create_post")
    with allure.step("Send POST request"):
        response = create_post("Hello from Python", "Body text", user_id=1)

    assert response.status_code == 201 , f"Expected status 202, but got {response.status_code}. Response body: {response.text}"
    logger.info("Test passed with id = %s", response.json().get("id"))
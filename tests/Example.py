from steps.post_steps import create_post
from utils.logger import logger


def test_create_post():
    logger.info("Starting test: create_post")
    response = create_post("Hello from Python", "Body text", user_id=1)

    assert response.status_code == 201 , f"Expected status 202, but got {response.status_code}. Response body: {response.text}"
    logger.info("Test passed with id = %s", response.json().get("id"))
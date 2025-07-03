import requests

from utils.env import BASE_URL
from utils.logger import logger


def create_post(title: str, body: str, user_id: int):
    logger.info("Sending POST request to /posts")
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    logger.debug("Response: %s", response.text)
    return response
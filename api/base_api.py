import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")

        if not self.base_url:
            raise ValueError("BASE_URL is not set")

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Python-Test-Suite/1.0"
        })

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)

        self._check_rate_limits(response)

        return response

    def _check_rate_limits(self, response):
        remaining = response.headers.get("X-RateLimit-Remaining")
        limit = response.headers.get("X-RateLimit-Limit")

        if remaining is not None:
            try:
                rem_int = int(remaining)
                if rem_int < 10:
                    logger.warning(
                        "Rate limit almost reached: %s remaining",
                        rem_int
                    )
            except (ValueError, TypeError):
                pass

    def get(self, endpoint, params=None, **kwargs):
        return self._send_request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, json=None, **kwargs):
        return self._send_request("POST", endpoint, json=json, **kwargs)
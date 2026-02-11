import os
import requests
import logging
import allure
import json
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class BaseAPI:
    DEFAULT_TIMEOUT = 5
    SENSITIVE_HEADERS = {"Authorization", "Cookie", "Set-Cookie", "X-Api-Key", "Token"}
    SENSITIVE_DATA_KEYS = {"email", "phone", "password", "address", "zipcode",
                           "street", "city", "iban", "bic", "birthday"
                           }

    def __init__(self):
        self.base_url = os.getenv("BASE_URL")

        if not self.base_url:
            raise ValueError("BASE_URL is not set in environment variables")

        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Python-Test-Suite/1.0"
        })

    def _mask_headers(self, headers):
        masked = dict(headers)
        for header in masked:
            if any(sensitive.lower() == header.lower() for sensitive in self.SENSITIVE_HEADERS):
                masked[header] = "********"
        return masked

    def _mask_body(self, data):
        if isinstance(data, dict):
            return {
                k: ("********" if k.lower() in self.SENSITIVE_DATA_KEYS else self._mask_body(v))
                for k, v in data.items()
            }
        elif isinstance(data, list):
            return [self._mask_body(item) for item in data]
        return data

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        timeout = kwargs.pop('timeout', self.DEFAULT_TIMEOUT)

        logger.info("Request: %s %s", method, url)

        try:
            with allure.step(f"HTTP {method} {endpoint}"):
                response = self.session.request(
                    method,
                    url,
                    timeout=timeout,
                    **kwargs
                )

                logger.info(
                    "Response: %s %s -> %s (%.3fs)",
                    method,
                    url,
                    response.status_code,
                    response.elapsed.total_seconds()
                )

                self._attach_to_allure(response)
                self._check_rate_limits(response)

                return response

        except requests.exceptions.RequestException as e:
            logger.error("Request failed: %s %s -> %s", method, url, str(e))
            allure.attach(str(e), name="Request Error", attachment_type=allure.attachment_type.TEXT)
            raise

    def _attach_to_allure(self, response):
        masked_req = self._mask_headers(response.request.headers)
        masked_res = self._mask_headers(response.headers)

        allure.attach(str(masked_req), name="Request Headers", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(masked_res), name="Response Headers", attachment_type=allure.attachment_type.TEXT)

        try:
            response_data = response.json()
            masked_body = self._mask_body(response_data)
            allure.attach(
                json.dumps(masked_body, indent=2),
                name="Response Body (Masked)",
                attachment_type=allure.attachment_type.JSON
            )
        except Exception:
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

    def _check_rate_limits(self, response):
        remaining = response.headers.get("X-RateLimit-Remaining")
        if remaining:
            try:
                if int(remaining) < 10:
                    logger.warning("Rate limit almost reached: %s remaining", remaining)
            except (ValueError, TypeError):
                pass

    def get(self, endpoint, params=None, **kwargs):
        return self._send_request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, json=None, **kwargs):
        return self._send_request("POST", endpoint, json=json, **kwargs)

    def put(self, endpoint, json=None, **kwargs):
        return self._send_request("PUT", endpoint, json=json, **kwargs)

    def patch(self, endpoint, json=None, **kwargs):
        return self._send_request("PATCH", endpoint, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._send_request("DELETE", endpoint, **kwargs)


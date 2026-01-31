import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint, params=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, **kwargs)

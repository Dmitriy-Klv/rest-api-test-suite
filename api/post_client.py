from api.base_api import BaseAPI

class PostClient(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = "/posts"

    def get_post(self, post_id: int):
        return self.get(f"{self.endpoint}/{post_id}")

    def get_all_posts(self):
        return self.get(self.endpoint)

    def create_post(self, payload: dict):
        return self.post(self.endpoint, json=payload)

    def update_post(self, post_id: int, payload: dict):
        return self.put(f"{self.endpoint}/{post_id}", json=payload)

    def patch_post(self, post_id: int, payload: dict):
        return self.patch(f"{self.endpoint}/{post_id}", json=payload)

    def delete_post(self, post_id: int):
        return self.delete(f"{self.endpoint}/{post_id}")

# methods for testing against reqres.in API
from http_client.client import HttpClient


class ReqResApiUtility:

    def __init__(self, base_url: str, timeout: int = 5, content_type: str = "json"):
        self.base_url = base_url
        self.client = HttpClient(base_uri=base_url)
        self.timeout = timeout
        
        # Set content type - defaults to JSON, but can be changed
        if content_type == "json":
            self.client.use_json()
        elif content_type == "xml":
            self.client.use_xml()
        elif content_type == "text":
            self.client.use_text()
        elif content_type == "urlencoded":
            self.client.use_urlencoded()

    def get_user(self, user_id: int):
        # Get a single user by ID
        response = self.client.get(f"/users/{user_id}")
        return response.json()

    def list_users(self, page: int = 1):
        # List users with pagination
        response = self.client.get("/users", params={"page": page})
        return response.json()

    def create_user(self, name: str, job: str):
        # Create a new user
        payload = {"name": name, "job": job}
        response = self.client.post("/users", data=payload)
        return response.json()

    def update_user(self, user_id: int, data: dict):
        # Update an existing user
        response = self.client.put(f"/users/{user_id}", data=data)
        return response.json()

    def delete_user(self, user_id: int):
        # Delete a user by ID
        response = self.client.delete(f"/users/{user_id}")
        return response


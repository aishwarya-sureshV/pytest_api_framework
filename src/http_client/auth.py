import base64


class AuthHelper:
    # Helper class providing authentication functionality

    def set_basic_auth(self, username: str, password: str):
        
        token = base64.b64encode(f"{username}:{password}".encode()).decode()
        self.auth_basic_header = f"Basic {token}"

    def set_api_key(self, api_key: str, header_name: str = "X-API-Key"):
        # Set API key authentication
        self.api_key = api_key
        self.api_key_header_name = header_name

    def set_csrf_token(self, token: str):
        # Set CSRF token authentication
        self.csrf_token = token

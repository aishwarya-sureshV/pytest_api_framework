from __future__ import annotations

import requests

from .auth import AuthHelper
from .content_type import ContentTypeHelper
from .helpers import HttpClientHelpers


class HttpClient(AuthHelper, ContentTypeHelper, HttpClientHelpers):
    """
    A reusable HTTP client built on top of requests.Session.
    Supports:
    - Base URI handling
    - Basic Authentication
    - API Key Authentication
    - CSRF Token Auth
    - Configurable content types
    - Cookie management
    """

    def __init__(self, base_uri: str = ""):
        self.base_uri = base_uri.rstrip("/") + "/"
        self.session = requests.Session()
        self.response = None
        self.csrf_token = None
        self.auth_basic_header = None
        self.content_type = None

    # --------------------------- HTTP methods ---------------------------

    def get(self, target: str = "/", params=None, headers=None):
        # Send GET request
        return self._send("GET", target, params=params, headers=self._headers(headers))

    def post(self, target: str = "/", data=None, headers=None, params=None):
        # Send POST request
        json_data = data if self.content_type == "application/json" else None
        body = None if json_data else data
        return self._send("POST", target, params=params, json=json_data, data=body,
                          headers=self._headers(headers))

    def patch(self, target: str = "/", data=None, headers=None, params=None):
        # Send PATCH request
        return self._send("PATCH", target, json=data, headers=self._headers(headers), params=params)

    def put(self, target: str = "/", data=None, headers=None, params=None):
        # Send PUT request
        return self._send("PUT", target, json=data, headers=self._headers(headers), params=params)

    def delete(self, target: str = "/", data=None, headers=None, params=None):
        # Send DELETE request
        return self._send("DELETE", target, json=data, headers=self._headers(headers), params=params)

    # --------------------------- Cookies ---------------------------

    @property
    def cookie_manager(self):
        # Access cookie manager
        return self.session.cookies

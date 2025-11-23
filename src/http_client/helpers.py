from urllib.parse import urljoin
import requests

from .exceptions import HttpRequestError


class HttpClientHelpers:

    def _url(self, target: str) -> str:
        # Construct full URL from base URI and target path
        return urljoin(self.base_uri, target.lstrip("/"))

    def _headers(self, headers=None):
        # Build headers dictionary with authentication and content type
        headers = headers.copy() if headers else {}

        if hasattr(self, 'auth_basic_header') and self.auth_basic_header:
            headers["Authorization"] = self.auth_basic_header

        if hasattr(self, 'api_key') and self.api_key:
            header_name = getattr(self, 'api_key_header_name', 'X-API-Key')
            headers[header_name] = self.api_key

        if hasattr(self, 'csrf_token') and self.csrf_token:
            headers["X-CSRF-Token"] = self.csrf_token

        if hasattr(self, 'content_type') and self.content_type:
            headers["Content-Type"] = self.content_type

        return headers

    def _send(self, method: str, target: str, **kwargs) -> requests.Response:
        # Send HTTP request and handle errors
        try:
            url = self._url(target)
            self.response = self.session.request(method, url, **kwargs)
            self.response.raise_for_status()
            return self.response
        except requests.HTTPError as e:
            # HTTPError includes status code information
            status_code = e.response.status_code if e.response else None
            raise HttpRequestError(
                str(e),
                url=url,
                method=method,
                status_code=status_code,
                original_exception=e
            )
        except requests.RequestException as e:
            # Other request exceptions (connection errors, timeouts, etc.)
            raise HttpRequestError(
                str(e),
                url=url,
                method=method,
                original_exception=e
            )

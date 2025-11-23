"""Webframe HTTP Client - A reusable HTTP client for API automation."""

from .client import HttpClient
from .exceptions import HttpRequestError

__all__ = ["HttpClient", "HttpRequestError"]

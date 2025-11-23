# Custom exceptions for the webframe HTTP client


class HttpRequestError(Exception):
    """
    Exception raised when an HTTP request fails.
    
    Provides useful context about the failed request including:
    - The original exception message
    - URL that was requested
    - HTTP method used
    - Status code (if available)
    """

    """Instead of just: "404 Client Error: Not Found"
    we get: "404 Client Error: Not Found | Request: GET https://api.example.com/users | Status Code: 404"
    """
    
    def __init__(self, message, url=None, method=None, status_code=None, original_exception=None):
        super().__init__(message)
        self.message = message
        self.url = url
        self.method = method
        self.status_code = status_code
        self.original_exception = original_exception
    
    def __str__(self):
        # Return a detailed error message
        parts = [self.message]
        
        if self.method and self.url:
            parts.append(f"Request: {self.method} {self.url}")
        
        if self.status_code:
            parts.append(f"Status Code: {self.status_code}")
        
        return " | ".join(parts)

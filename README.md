# PyTest API Automation Framework

A production-ready API testing framework built with Python and PyTest. This framework provides a reusable HTTP client library and comprehensive test utilities for API automation, demonstrated using the ReqRes API.

## Overview

This framework is designed with best practices in mind, featuring a modular architecture, clean separation of concerns, and extensible design patterns. It serves as both a practical testing solution and a reference implementation for API automation projects.

## Features

### HTTP Client Library (`http_client`)

A robust, reusable HTTP client built on top of `requests.Session` with the following capabilities:

- **Base URI Management**: Automatic URL construction with base URI support
- **Multiple Authentication Methods**:
  - Basic Authentication (username/password)
  - API Key Authentication (customizable header name)
  - CSRF Token Authentication
- **Content Type Configuration**: Support for JSON, XML, Text, and URL-encoded formats
- **Cookie Management**: Built-in session cookie handling
- **Error Handling**: Custom exceptions with detailed error context (URL, method, status code)
- **HTTP Methods**: Full support for GET, POST, PUT, PATCH, and DELETE requests
- **Modular Architecture**: Separated into logical modules (auth, content types, helpers) using mixin pattern

### Test Framework

- **Pytest Integration**: Full PyTest support with fixtures and markers
- **Custom Markers**: `@pytest.mark.smoke` and `@pytest.mark.integration` for test categorization
- **Reusable Fixtures**: Pre-configured HTTP clients and test data fixtures
- **API-Specific Utilities**: Dedicated utility classes for specific APIs (e.g., ReqResApiUtility)
- **Centralized Configuration**: Test constants and configuration in dedicated modules

## Project Structure

```
pytest_api_framework/
├── src/
│   └── http_client/              # Reusable HTTP client library
│       ├── __init__.py           # Package exports
│       ├── client.py             # Main HttpClient class
│       ├── auth.py               # Authentication helpers (Basic, API Key, CSRF)
│       ├── content_type.py       # Content type configuration helpers
│       ├── helpers.py            # Internal helper methods (URL construction, headers, request sending)
│       └── exceptions.py         # Custom exception classes
│
├── tests/                        # Test suite
│   ├── conftest.py               # Pytest fixtures and configuration
│   ├── test_users.py             # Test cases for user management API
│   └── helpers/                  # Test helper utilities
│       ├── __init__.py
│       └── api/
│           ├── __init__.py
│           ├── reqres_api_utility.py  # ReqRes API wrapper class
│           └── constants.py            # Test configuration constants
│
├── requirements.txt              # Python dependencies
├── setup.py                     # Package setup configuration
├── pytest.ini                   # Pytest configuration
├── pyproject.toml               # Modern Python project configuration
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate          # Windows PowerShell
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode** (optional):
   ```bash
   pip install -e .
   ```

## Quick Start

### Running Tests

Run all tests:
```bash
pytest
```

Run with quiet output:
```bash
pytest -q
```

Run only smoke tests:
```bash
pytest -m smoke
```

Run only integration tests:
```bash
pytest -m integration
```

### Using the HTTP Client

```python
from http_client.client import HttpClient

# Create a client with base URI
client = HttpClient(base_uri="https://api.example.com")

# Configure authentication
client.set_api_key("your-api-key", header_name="X-API-Key")
client.set_basic_auth("username", "password")

# Set content type
client.use_json()

# Make requests
response = client.get("/users")
response = client.post("/users", data={"name": "John", "email": "john@example.com"})
response = client.put("/users/1", data={"name": "Jane"})
response = client.delete("/users/1")
```

### Using API Utilities

```python
from tests.helpers.api.reqres_api_utility import ReqResApiUtility
from tests.helpers.api import constants

# Create API utility instance
api = ReqResApiUtility(
    base_url=constants.BASE_URL,
    timeout=constants.TEST_TIMEOUT,
    content_type="json"
)

# Use API methods
user = api.get_user(user_id=2)
users = api.list_users(page=1)
new_user = api.create_user(name="John Doe", job="Engineer")
updated = api.update_user(user_id=1, data={"name": "Jane Doe"})
api.delete_user(user_id=1)
```

## Architecture

### Design Patterns

1. **Mixin Pattern**: Authentication and content type functionality separated into helper classes using multiple inheritance
2. **Separation of Concerns**: Source code (`src/`), tests (`tests/`), and utilities clearly separated
3. **Dependency Injection**: Fixtures provide dependencies to test functions
4. **DRY Principle**: Reusable components and utilities to avoid code duplication

### HTTP Client Architecture

The `HttpClient` class combines functionality from three helper classes:

- **AuthHelper**: Provides authentication methods (Basic, API Key, CSRF Token)
- **ContentTypeHelper**: Manages content type configuration
- **HttpClientHelpers**: Contains internal methods for URL construction, header building, and request sending

This modular approach makes the codebase maintainable and extensible.

### Error Handling

The framework includes a custom `HttpRequestError` exception that provides detailed context:

```python
try:
    client.get("/invalid-endpoint")
except HttpRequestError as e:
    print(e)
    # Output: "404 Client Error: Not Found | Request: GET https://api.example.com/invalid-endpoint | Status Code: 404"
```

## Test Examples

The framework includes comprehensive test examples covering:

- **GET Operations**: Retrieving single and multiple resources
- **POST Operations**: Creating new resources
- **PUT Operations**: Updating existing resources
- **DELETE Operations**: Removing resources
- **Error Handling**: Testing error scenarios
- **Integration Flows**: End-to-end workflows (create → update → delete)

All tests use PyTest fixtures for clean, maintainable test code.

## Configuration

### Pytest Configuration (`pytest.ini`)

- Test paths: `tests/`
- Python path: `src/` (for importing `http_client` package)
- Custom markers: `smoke`, `integration`
- Default options: Quiet mode (`-q`)

### Test Constants (`tests/helpers/api/constants.py`)

Centralized configuration for test-specific constants:
- `BASE_URL`: API base URL
- `TEST_TIMEOUT`: Request timeout in seconds

## Extending the Framework

### Adding New API Utilities

1. Create a new utility class in `tests/helpers/api/`:
   ```python
   from http_client.client import HttpClient
   
   class MyApiUtility:
       def __init__(self, base_url: str):
           self.client = HttpClient(base_uri=base_url)
           self.client.use_json()
       
       def my_api_method(self):
           response = self.client.get("/endpoint")
           return response.json()
   ```

2. Create a fixture in your test file:
   ```python
   @pytest.fixture
   def my_api_client():
       return MyApiUtility(base_url="https://api.example.com")
   ```

### Adding New Tests

1. Create test files in `tests/` directory
2. Use fixtures from `conftest.py` or create test-specific fixtures
3. Apply markers (`@pytest.mark.smoke`, `@pytest.mark.integration`) as needed

### Adding New Authentication Methods

Extend `AuthHelper` class in `src/http_client/auth.py`:
```python
def set_custom_auth(self, token: str):
    self.custom_token = token
```

Update `_headers()` method in `helpers.py` to include the new authentication.

## Best Practices Implemented

- ✅ **Standard Project Structure**: Follows Python packaging best practices
- ✅ **Type Hints**: Simplified type annotations for beginner-friendliness
- ✅ **Modular Design**: Separated concerns with dedicated modules
- ✅ **Error Handling**: Comprehensive exception handling with context
- ✅ **Documentation**: Clear docstrings and comments
- ✅ **Test Organization**: Logical test structure with markers
- ✅ **Configuration Management**: Centralized constants and configuration
- ✅ **Reusability**: DRY principles applied throughout

## Dependencies

- **pytest** (>=7.0): Testing framework
- **requests** (>=2.0.0): HTTP library
- **allure-pytest** (>=2.9.45): Test reporting (optional)
- **setuptools** (>=45): Package management

## Reporting (Optional)

Generate Allure reports:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## License

See [LICENSE](LICENSE) file for details.

## Author

Aishwarya Suresh

---

**Note**: This framework uses the public ReqRes API (https://reqres.in/) for demonstration purposes. No authentication is required to run the tests.

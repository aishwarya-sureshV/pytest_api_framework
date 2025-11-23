# PyTest API Automation Framework

A production-ready API testing framework built with Python and PyTest. Provides a reusable HTTP client library and test utilities for API automation, demonstrated using the ReqRes API.

## Features

**HTTP Client Library**
- Base URI management with automatic URL construction
- Multiple authentication methods (Basic, API Key, CSRF Token)
- Content type support (JSON, XML, Text, URL-encoded)
- Cookie management and session handling
- Custom exceptions with detailed error context
- Full HTTP method support (GET, POST, PUT, PATCH, DELETE)
- Modular architecture using mixin pattern

**Test Framework**
- PyTest integration with fixtures and markers
- Custom markers (`@pytest.mark.smoke`, `@pytest.mark.integration`)
- Reusable fixtures and API-specific utilities
- Centralized configuration management

## Project Structure

```
pytest_api_framework/
├── src/http_client/          # HTTP client library
│   ├── client.py             # Main HttpClient class
│   ├── auth.py               # Authentication helpers
│   ├── content_type.py       # Content type configuration
│   ├── helpers.py            # Internal helper methods
│   └── exceptions.py         # Custom exceptions
├── tests/                    # Test suite
│   ├── conftest.py           # Pytest fixtures
│   ├── test_users.py         # Test cases
│   └── helpers/api/          # API utilities
│       ├── reqres_api_utility.py
│       └── constants.py
├── requirements.txt
├── setup.py
├── pytest.ini
└── pyproject.toml
```

## Installation

**Prerequisites**: Python 3.9+ and pip

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Optional: development mode
   ```

## Quick Start

**Running Tests**
```bash
pytest              # Run all tests
pytest -q           # Quiet output
pytest -m smoke     # Smoke tests only
pytest -m integration  # Integration tests only
```

**Using the HTTP Client**
```python
from http_client.client import HttpClient

client = HttpClient(base_uri="https://api.example.com")
client.set_api_key("your-api-key", header_name="X-API-Key")
client.use_json()

response = client.get("/users")
response = client.post("/users", data={"name": "John", "email": "john@example.com"})
response = client.put("/users/1", data={"name": "Jane"})
response = client.delete("/users/1")
```

**Using API Utilities**
```python
from tests.helpers.api.reqres_api_utility import ReqResApiUtility
from tests.helpers.api import constants

api = ReqResApiUtility(base_url=constants.BASE_URL, timeout=constants.TEST_TIMEOUT, content_type="json")
user = api.get_user(user_id=2)
users = api.list_users(page=1)
new_user = api.create_user(name="John Doe", job="Engineer")
```

## Architecture

**Design Patterns**
- Mixin pattern for authentication and content type functionality
- Separation of concerns (source, tests, utilities)
- Dependency injection via fixtures
- DRY principles : Reusable components and utilities to avoid code duplication

**HTTP Client Structure**
- `AuthHelper`: Authentication methods (Basic, API Key, CSRF Token)
- `ContentTypeHelper`: Content type configuration
- `HttpClientHelpers`: URL construction, headers, request sending

**Error Handling**
```python
try:
    client.get("/invalid-endpoint")
except HttpRequestError as e:
    print(e)  # Detailed error context with URL, method, status code
```

## Test Examples

Comprehensive test coverage: GET, POST, PUT, DELETE operations, error handling, and integration flows. All tests use PyTest fixtures.

## Configuration

**Pytest** (`pytest.ini`): Test paths, Python path, custom markers (`smoke`, `integration`)

**Test Constants** (`tests/helpers/api/constants.py`): `BASE_URL`, `TEST_TIMEOUT`

## Extending the Framework

**Adding New API Utilities**
```python
from http_client.client import HttpClient

class MyApiUtility:
    def __init__(self, base_url: str):
        self.client = HttpClient(base_uri=base_url)
        self.client.use_json()
    
    def my_api_method(self):
        return self.client.get("/endpoint").json()
```

**Adding New Tests**: Create test files in `tests/`, use fixtures from `conftest.py`, apply markers as needed.

**Adding New Authentication**: Extend `AuthHelper` in `src/http_client/auth.py` and update `_headers()` in `helpers.py`.

## Best Practices

- ✅ **Standard Project Structure**: Follows Python packaging best practices
- ✅ **Type Hints**: Simplified type annotations for beginner-friendliness
- ✅ **Modular Design**: Separated concerns with dedicated modules
- ✅ **Error Handling**: Comprehensive exception handling with context
- ✅ **Documentation**: Clear docstrings and comments
- ✅ **Test Organization**: Logical test structure with markers
- ✅ **Configuration Management**: Centralized constants and configuration
- ✅ **Reusability**: DRY principles applied throughout

## Dependencies

- pytest (>=7.0)
- requests (>=2.0.0)
- allure-pytest (>=2.9.45, optional)
- setuptools (>=45)

```

## License

See [LICENSE](LICENSE) file for details.

**Note**: This framework uses the public ReqRes API (https://reqres.in/) for demonstration purposes. No authentication is required.

# REST API Test Automation Suite

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/tested%20with-pytest-0f0?logo=pytest)](https://pytest.org/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-blue)](https://docs.pydantic.dev/latest/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A technical demonstration of an automated testing framework for RESTful APIs. This project implements a modular architecture using Python, focusing on contract testing and data integrity validation.

## 🌐 Target Service Specification
This project demonstrates  API testing skills using the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) public API.   

## 📂 Project Structure
```text
rest-api-test-suite/
│
├── api/
│   ├── base_api.py          # Base API client (session, headers, request handling)
│   └── post_client.py       # Posts API client
│
├── models/
│   └── post_model.py        # Pydantic models for response validation
│
├── tests/
│   └── posts/
│       ├── test_get_posts_validation.py
│       ├── test_get_posts_behavior.py
│       ├── test_get_posts_headers.py
│       └── test_get_posts_performance.py
│
├── .env                     # Environment variables (BASE_URL)
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md                # Project documentation

```


## ⚙️ Technical Specifications
* **Core:** Python 3.10+
* **Test Engine:** `pytest`
* **Validation Layer:** `Pydantic v2` (Runtime type checking)
* **HTTP Protocol:** `requests`
* **Configuration:** `python-dotenv` (Management of environment variables)


## 🚀 Installation & Usage
**Environment Setup:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
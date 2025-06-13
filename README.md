# API Tests with Pytest + Requests

Autotests for public REST API [`jsonplaceholder.typicode.com`](https://jsonplaceholder.typicode.com) using `pytest` and `requests`.

## Project structure
├── tests/
│ ├── test_users.py
│ └── test_parameterization.py
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore


## How to run
pip install -r requirements.txt
pytest -v


## Test coverage:
GET /users
POST /users
PUT /users/1
DELETE /users/1
Negative cases
Parametrize
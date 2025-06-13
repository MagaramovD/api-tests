# API Tests with Pytest + Requests

Autotests for public REST API [`jsonplaceholder.typicode.com`](https://jsonplaceholder.typicode.com) using **pytest** and **requests**.

---

## Project Structure

```
tests/
├── test_users.py
├── test_parameterization.py
conftest.py
requirements.txt
README.md
.gitignore
```

---

## How to Run

```bash
pip install -r requirements.txt
pytest -v
```

---

## Test Coverage

- `GET /users`
- `POST /users`
- `PUT /users/1`
- `DELETE /users/1`
- Negative cases
- Parametrize

<<<<<<< HEAD
---
=======
---
>>>>>>> 3d40ae8c202d1148772714cfadd11f936335ebf9

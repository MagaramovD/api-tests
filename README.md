# 🧪 Automation Testing Project — API + UI

Autotests for:

- Public REST API [`jsonplaceholder.typicode.com`](https://jsonplaceholder.typicode.com)
- Web UI [`saucedemo.com`](https://www.saucedemo.com)

Built using **pytest**, **requests**, and **playwright**.

---

## 📁 Project Structure

```
project/
├── pages/
│   └── login_page.py         # Page Object Model for saucedemo login
├── tests/
│   ├── test_users.py         # API tests
│   ├── test_parameterization.py # Parametrized API tests
│   └── test_ui.py            # UI tests for saucedemo.com
├── __init__.py               # marks folder as a module
conftest.py                   # fixtures (e.g. base URL)
requirements.txt              # dependencies
README.md                     # you're reading it
.gitignore                    # excludes cache, venv, etc.
```

---

## ▶ How to Run

```bash
pip install -r requirements.txt
pytest -v
```

---

## ✅ Test Coverage

### API Tests
- `GET /users`
- `POST /users`
- `PUT /users/1`
- `DELETE /users/1`
- Negative cases
- Parametrized tests

### UI Tests
- Login success with Page Object Model
- Login with locked user
- Wrong username and empty field validation

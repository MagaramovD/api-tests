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
├── test_parameterization.py  # Parametrized API tests
│   └── test_ui.py            # UI tests for saucedemo.com
├── __init__.py               # marks folder as a module
conftest.py                   # fixtures (e.g. base URL)
requirements.txt              # dependencies
README.md                     # you're reading it
.gitignore                    # excludes cache, venv, etc.
```

---

## ▶ How to Run Locally

```bash
pip install -r requirements.txt
python -m playwright install
pytest project/tests --alluredir=allure-results
allure serve allure-results
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

---

## 📦 CI/CD

- Tests are automatically executed on **GitHub Actions** on every push.
- **Python version:** `3.12.10`
- **OS:** `ubuntu-latest`
- **Browsers:** Installed dynamically via `playwright install`
- **Artifacts:** (like Allure results) are uploaded after the run

---

## 🌐 Live Allure Report

You can view the latest HTML report hosted on GitHub Pages here:

🔗 **[Open Allure Report](https://magaramovd.github.io/api-tests/)**

---

## 🛑 Notes

- The `allure-results` folder is included in the CI workflow but **not committed** to the repo.
- The `allure-report` is **automatically deployed** to `gh-pages` branch after successful test run.

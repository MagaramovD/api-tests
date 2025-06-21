from playwright.sync_api import Page
from project.pages.login_page import LoginPage
import allure


# Playwr

@allure.dynamic.title("Successful login with valid credentials")
@allure.dynamic.severity(allure.severity_level.CRITICAL)
@allure.dynamic.description("This test verifies that a user can log in using correct credentials.")
@allure.dynamic.tag("UI", "Login")
def test_login(page: Page, saucedemo_url):
    with allure.step("Enter to website"):
        page.goto(saucedemo_url)
    assert "Swag Labs" in page.title()
    with allure.step("Fill username and password"):
        user_name = page.locator('#user-name')
        password = page.locator('#password')
        user_name.fill("problem_user")
        password.fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    assert page.locator(
        '[data-test="title"]').is_visible(), "Login failed or Products title not visible"
    page.locator('[data-test="inventory-item-name"]',
                 has_text="Sauce Labs Backpack").click()
    assert page.locator(
        '[data-test="inventory-item-name"]').is_visible(), "Login failed or Products not visible"


@allure.title("Successful login with valid credentials using POM")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test verifies that a user can log in using correct credentials using POM.")
@allure.tag("UI", "Login")
def test_login_with_object(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    login_page = LoginPage(page)
    login_page.login("problem_user", "secret_sauce")
    assert page.locator(
        '[data-test="title"]').is_visible(), "Login failed or Products title not visible"
    page.locator('[data-test="inventory-item-name"]',
                 has_text="Sauce Labs Backpack").click()
    assert page.locator(
        '[data-test="inventory-item-name"]').is_visible(), "Login failed or Products not visible"


# Negative tests
@allure.title("Unsuccessful login with valid credentials of locked user ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test verifies that a user can log in using correct credentials of locked user")
@allure.tag("UI", "Login")
def test_login_locked_user(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error message not visible"
    page.screenshot(path="screenshots/locked_user_error.png", full_page=True)


@allure.title("Unsuccessful login with empty user name. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test verifies that a user can't login without user name")
@allure.tag("UI", "Login")
def test_login_empty_username(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    page.locator('#password').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error for empty username"
    page.screenshot(
        path="screenshots/empty_username_error.png", full_page=True)


@allure.title("Unsuccessful login with no valid user name. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test verifies that a user can't login with unvalid username")
@allure.tag("UI", "Login")
def test_unexist_username(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    login_page = LoginPage(page)
    login_page.login("locked_out_user12", "secret_sauce")
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error message not visible"
    page.screenshot(
        path="screenshots/wrong_username_error.png", full_page=True)

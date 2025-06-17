from playwright.sync_api import Page
from project.pages.login_page import LoginPage


# Playwr


def test_login(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    assert "Swag Labs" in page.title()
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

def test_login_locked_user(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error message not visible"
    page.screenshot(path="screenshots/locked_user_error.png", full_page=True)


def test_login_empty_username(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    page.locator('#password').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error for empty username"
    page.screenshot(
        path="screenshots/empty_username_error.png", full_page=True)


def test_username(page: Page, saucedemo_url):
    page.goto(saucedemo_url)
    login_page = LoginPage(page)
    login_page.login("locked_out_user12", "secret_sauce")
    assert page.locator(
        '[data-test="error"]').is_visible(), "Expected error message not visible"
    page.screenshot(
        path="screenshots/wrong_username_error.png", full_page=True)

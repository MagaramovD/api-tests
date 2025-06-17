
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('[data-test="login-button"]')

    def login(self, user, password):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

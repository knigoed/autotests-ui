from operator import index

from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email' )
        self.password_input = Input(page,'login-form-password-input', 'Password' )

    def fill(self, email: str, password: str):
        self.email_input.fill(email, index=index)
        self.email_input.check_have_value(email, index=index)

        self.password_input.fill(password, index=index)
        self.password_input.check_have_value(password, index=index)

    def check_visible(self, email: str, password: str):
        self.email_input.check_visible(index=index)
        self.email_input.check_have_value(email, index=index)

        self.password_input.check_visible(index=index)
        self.password_input.check_have_value(password, index=index)




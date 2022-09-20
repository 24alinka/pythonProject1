from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_up(self, username, email, password):
        """Sign up as the user"""
        # Fill Sign Up
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

        sleep(1)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(1)

    def error_name(self, username):
        """Sign Up with invalid name"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)

    def error_password(self, password):
        """Sign Up with invalid password"""
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

    def error_email(self, email):
        """Sign up twice with the same email"""
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)

    def verify_email_error(self):
        """Verify invalid Email error"""
        assert self.get_element_text(
            self.constants.HINT_EMAIL_ERROR_XPATH) == self.constants.HINT_EMAIL_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_EMAIL_ERROR_XPATH)}"

    def verify_password_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_PASSWORD_XPATH) == self.constants.HINT_PASSWORD_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_PASSWORD_XPATH)}"

    def verify_name_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_NAME_ERROR_XPATH) == self.constants.HINT_NAME_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_NAME_ERROR_XPATH)}"

    def verify_success_sign_up(self, username):
        """Verify success Sign Up using hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(
            username=username), \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}"

        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"

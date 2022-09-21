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
        sleep(2)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(2)

    def verify_success_sign_up(self, username):
        """Verify success Sign Up using hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(
            username=username), \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}"

        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"

    def error_name(self):
        """Sign Up with invalid name"""
        # Fill Sign Up
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=" ")
        sleep(2)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(2)

    def verify_name_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_NAME_ERROR_XPATH) == self.constants.HINT_NAME_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_NAME_ERROR_XPATH)}"

    def error_password(self):
        """Sign Up with invalid password"""
        # Fill Sign Up
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=" ")
        sleep(2)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(2)

    def verify_password_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_PASSWORD_XPATH) == self.constants.HINT_PASSWORD_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_PASSWORD_XPATH)}"

    def error_email(self):
        """Sign up twice with the same email"""
        # Fill Sign Up
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=" ")
        sleep(2)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(2)

    def verify_email_error(self):
        """Verify twice same Email error"""
        assert self.get_element_text(
            self.constants.HINT_EMAIL_XPATH2) == self.constants.HINT_EMAIL_TEXT2, \
            f"Actual message: {self.get_element_text(self.constants.HINT_EMAIL_XPATH2)}"

    def verify_email_error2(self):
        """Verify invalid  Email error"""
        assert self.get_element_text(
            self.constants.HINT_EMAIL_XPATH) == self.constants.HINT_EMAIL_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_EMAIL_XPATH)}"

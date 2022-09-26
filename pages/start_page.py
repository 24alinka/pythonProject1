from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import wait_until_ok


# from pages.hello_page import HelloPage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()
        self.header = Header(self.driver)
        # self.hello_page = HelloPage(self.driver)

    def sign_up_and_verify(self, username, email, password):
        """Sign up as the user and verify that you're inside"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        self.click_sign_up_and_verify()
        # Return new page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok(period=0.5)
    def click_sign_up_and_verify(self):
        """Click Sign Up button and verify"""
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def sign_up_and_fail(self, login, email, password):
        """Sign up as the user. Only for incorrect Sign Up"""
        # Fill Username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=login)
        # Fill email
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_name_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_NAME_ERROR_XPATH) == self.constants.HINT_NAME_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_NAME_ERROR_XPATH)}"

    def verify_password_error(self):
        """Verify invalid Password error"""
        assert self.get_element_text(
            self.constants.HINT_PASSWORD_XPATH) == self.constants.HINT_PASSWORD_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_PASSWORD_XPATH)}"

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

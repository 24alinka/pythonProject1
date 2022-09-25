from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

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

    def error_name(self):
        """Sign Up with invalid name"""
        # Fill Sign Up
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=" ")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=" ")
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

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
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

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
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

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

    def sign_in(self, username, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_incorrect_sign_in(self):
        """Sign In with invalid username / password"""
        assert self.get_element_text(
            self.constants.HINT_SIGN_IN_XPATH) == self.constants.HINT_SIGN_IN_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.HINT_SIGN_IN_XPATH)}"

    def successful_login_and_verify(self, username, password):
        """
        - Login with previously registered data
        - After successful login -> hello message
        """
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        # Return new page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

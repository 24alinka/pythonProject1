from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.hello_page import HelloPage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()
        self.hello_page = HelloPage(self.driver)

    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

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

    def sign_out(self):
        """Click on sign out from profile"""
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        assert not self.is_exists(self.constants.CREATE_POST_BUTTON_XPATH)
        assert self.get_element_text(self.constants.SIGN_OUT_BUTTON_XPATH) == self.constants.SIGN_IN_BUTTON_TEXT

    def verify_sign_out_success(self):
        """Verify correct Sign Out"""
        assert not self.is_exists(self.constants.ACCOUNT_NAME_XPATH)
        assert self.get_element_text(self.constants.SIGN_IN_BUTTON_XPATH) == self.constants.SIGN_IN_BUTTON_TEXT

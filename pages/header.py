from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()
        from constants.create_post_page import CreatePostPageConsts
        self.constants2 = CreatePostPageConsts()

    @log_decorator
    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    @log_decorator
    def open_chat_page(self):
        self.click(xpath=self.constants.CHAT_XPATH)
        from pages.chat_page import ChatPage
        return ChatPage(self.driver)

    @log_decorator
    def sign_out_click(self):
        """Sign Out from Hello page"""
        # Click button
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_decorator
    def search_previously_created_post(self, post, user):
        self.click(xpath=self.constants.SEARCH_XPATH)
        self.fill_field(xpath=self.constants.INPUT_SEARCH, value=post.title)
        self.click(xpath=self.constants.SEARCH_RESULT_XPATH.format(title_of_post=post.title))
        self.click(xpath=self.constants2.CLICK_ON_PROFILE_FROM_POST_XPATH.format(username=user.username))

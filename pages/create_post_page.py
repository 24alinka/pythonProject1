from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()
        from pages.header import Header
        self.header = Header(self.driver)

    @log_decorator
    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_successfully_created(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def delete_post(self):
        """Delete a post that was made"""
        self.click(xpath=self.constants.DELETE_POST_XPATH)

    @log_decorator
    def verify_successfully_delete_post(self):
        """Verify the post is successfully deleted message"""
        assert self.get_element_text(
            xpath=self.constants.SUCCESS_DELETE_MESSAGE_XPATH) == self.constants.SUCCESS_DELETE_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.SUCCESS_DELETE_MESSAGE_XPATH)}"

    @log_decorator
    def click_edit_post(self):
        """Edit post"""
        self.click(xpath=self.constants.EDIT_POST_BUTTON_XPATH)

    @log_decorator
    def edit_post(self, title, body):
        """Update post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.UPDATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_successfully_edit_post(self):
        """Verify that the body us updated and message appears"""
        assert self.get_element_text(xpath=self.constants.EDIT_MESSAGE_XPATH) == self.constants.EDIT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.EDIT_MESSAGE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH) == self.constants.UPDATE_POST_BODY_TEXT
        f"Actual message: {self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH)}"

    @log_decorator
    def create_post_with_click_checkbox(self, post):
        """Create a unique post with checkbox"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.CHECKBOX_XPATH)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def select(self, post, select_value):
        """Open select and choose a value"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.select_field(xpath=self.constants.POST_SELECT_XPATH, value=select_value)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_private_option(self):
        """Verify the post is private message"""
        assert self.get_element_text(
            xpath=self.constants.POST_SELECT_PRIVATE_XPATH) == self.constants.POST_SELECT_PRIVATE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.POST_SELECT_PRIVATE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def verify_group_message_option(self):
        """Verify the post is private message"""
        assert self.get_element_text(
            xpath=self.constants.POST_SELECT_GROUP_MESSAGE_XPATH) == self.constants.POST_SELECT_GROUP_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.POST_SELECT_GROUP_MESSAGE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def verify_all_users_option(self):
        """Verify the post is private message"""
        assert self.get_element_text(
            xpath=self.constants.POST_SELECT_ALL_USERS_XPATH) == self.constants.POST_SELECT_ALL_USERS_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.POST_SELECT_ALL_USERS_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def create_post_with_all(self, post):
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.select_field(xpath=self.constants.POST_SELECT_XPATH, value=post.select)
        self.click(xpath=self.constants.CHECKBOX_XPATH)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_create_full_post(self, title, body):
        assert self.get_element_text(
            xpath=self.constants.POST_SELECT_PRIVATE_XPATH) == self.constants.POST_SELECT_PRIVATE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.POST_SELECT_PRIVATE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"
        assert self.get_element_text(
            xpath=self.constants.UNIQUE_MESSAGE_YES_XPATH) == self.constants.UNIQUE_MESSAGE_YES_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.UNIQUE_MESSAGE_YES_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SAVED_POST_TITLE_XPATH) == title, \
            f"Actual: {self.get_element_text(xpath=self.constants.SAVED_POST_TITLE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.SAVED_POST_BODY_XPATH) == body, \
            f"Actual: {self.get_element_text(xpath=self.constants.SAVED_POST_BODY_XPATH)}"

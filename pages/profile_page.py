from pages.base_page import BasePage


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        from constants.profile_page import ProfilePageConsts
        self.constants = ProfilePageConsts
        from pages.header import Header
        self.header = Header(self.driver)

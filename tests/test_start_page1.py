import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        yield StartPage(driver)
        driver.close()

    def test_incorrect_name_sign_up(self, start_page):
        # Fill UserName
        user = random_str()
        username_value = "test test"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        start_page.sign_up_and_fail(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify name error
        start_page.verify_name_error()
        self.log.info("Error was verified")

    def test_incorrect_password_sign_up(self, start_page):
        # Fill Password
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}"
        start_page.sign_up_and_fail(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify password error
        start_page.verify_password_error()
        self.log.info("Error was verified")

    def test_valid_data_sign_up(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        hello_page = start_page.sign_up_and_verify(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify success message
        hello_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")

    def test_invalid_email_sign_up(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up_and_fail(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify error message
        start_page.verify_email_error2()
        self.log.info("Error was verified")

    def test_same_email_sign_up(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = "testalinka-tets@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up_and_fail(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify error message
        start_page.verify_email_error()
        self.log.info("Error was verified")

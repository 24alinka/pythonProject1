import logging
from time import sleep

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
        yield StartPage(driver)
        driver.close()

    def test_incorrect_name(self, start_page):
        # Fill UserName
        user = random_str()
        username_value = "test test"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        sleep(2)
        # Verify name error
        start_page.verify_name_error()
        self.log.info("Error was verified")

    def test_incorrect_password(self, start_page):
        # Fill Password
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}"
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        # Verify password error
        start_page.verify_password_error()
        self.log.info("Error was verified")

    def test_valid_data(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        sleep(2)
        # Verify success message
        start_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")

    def test_invalid_email(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        sleep(2)
        # Verify error message
        start_page.verify_email_error()
        self.log.info("Error was verified")

    def test_same_email(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = "testalinka-tets@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)
        sleep(2)
        # Verify error message
        start_page.verify_email_error()
        self.log.info("Error was verified")

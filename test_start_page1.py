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
        yield StartPage(driver)
        driver.close()

    def test_incorrect_name(self, start_page):
        # Fill UserName
        start_page.error_name("test test")
        self.log.info("Please enter a valid name")

        # Verify name error
        start_page.verify_name_error()
        self.log.info("Error was verified")

    def test_incorrect_password(self, start_page):
        # Fill Password
        start_page.error_password("test")
        self.log.info("Please enter a valid password")

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

        # Verify success message
        start_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")

    def test_invalid_email(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = start_page.error_email("testalinka-tets@@gmail.com")
        password_value = f"{random_str(6)}{random_num()}"
        # Sign Up as a user
        start_page.sign_up(username_value, password_value, email_value)
        self.log.info("Signed Up as user %s", email_value)
        # Verify error message
        start_page.verify_email_error(email_value)
        self.log.info("You must provide a valid email address")

    def test_same_email(self, start_page):
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = start_page.error_email("testalinka-tets@gmail.com")
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify error message
        start_page.verify_email_error(email_value)
        self.log.info("That email is already being used.")

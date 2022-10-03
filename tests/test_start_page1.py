import logging

<<<<<<< HEAD
from pages.utils import User
=======
import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num
>>>>>>> origin/homework


class TestStartPage:
    log = logging.getLogger("[StartPage]")

<<<<<<< HEAD
    def test_incorrect_name(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill incorrect name
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Fill UserName
        user = User()
        user.fill_data(username="ttest tset")
        # Sign Up as a user
        start_page.click_sign_up_not_valid(user)
        # Verify error message
        start_page.verify_name_error()
        self.log.info("Error was verified")

    def test_incorrect_password(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill name
            - Fill login
            - Fill incorrect password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        user = User()
        user.fill_data(password="ttesttset")
        # Sign Up as a user
        start_page.click_sign_up_not_valid(user)
        # Verify error message
        start_page.verify_password_error()
        self.log.info("Error was verified")

    def test_valid_data(self, start_page, random_user):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill name
            - Fill login
            - Fill password
            - Click button
            - Verify success sign up
        - Post-conditions:
            - Close driver
        """
        # Sign Up as a user
        hello_page = start_page.sign_up_and_verify(random_user)

        # Verify success message
        hello_page.verify_success_sign_up(random_user.username)

    def test_invalid_email(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill name
            - Fill incorrect login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Prepare data
        user = User()
        user.fill_data(email="test@@test.estst")
        # Sign Up as a user
        start_page.click_sign_up_not_valid(user)
=======
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
>>>>>>> origin/homework
        # Verify error message
        start_page.verify_email_error2()
        self.log.info("Error was verified")

<<<<<<< HEAD
    def test_same_email(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill name
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Prepare data
        user = User()
        user.fill_data(email="testalinka-tets@gmail.com")
        # Sign Up as a user
        start_page.click_sign_up_not_valid(user)
        # Verify error message
        start_page.verify_email_error()
        self.log.info("Error was verified")

    def test_incorrect_login(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill login
            - Fill password
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Login as a user
        start_page.sign_in("Alinka111", "testtesttsetestset")
        self.log.info("Logged in as non-existing user")
        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_empty_login(self, start_page):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify error
        """
        # Login as a user
        start_page.sign_in("", "")
        self.log.info("Logged in as non-existing user")
        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_valid_login(self, start_page):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify Successful login
        """
        hello_page = start_page.sign_in_and_verify("tsetAlinkaTest", "testtesttest")
        self.log.info("Username with valid data")
        # Verify successful Login
        hello_page.verify_success_sign_up(username="tsetAlinkaTest")
        self.log.info("Hello message was verified")
=======
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
>>>>>>> origin/homework

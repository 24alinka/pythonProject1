import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


class TestsHeader:
    log = logging.getLogger("[Header]")

    @pytest.fixture(scope="function")
    def start_page(self):
        """Open start page"""
        # create driver
        driver = webdriver.Chrome(DRIVER_PATH)
        # open Start Page URL
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Close driver
        driver.close()

    def test_incorrect_login(self, start_page):
        start_page.header.sign_in("testtest11", "123456789testt")
        self.log.info("Logged in as non-existing user")
        # Verify error
        start_page.header.verify_incorrect_sign_in()
        self.log.info("Error was verified")

    def test_valid_login(self, start_page):
        hello_page = start_page.header.sign_in("tsetAlinkaTest", "testtesttest")
        self.log.info("Username with valid data")
        # Verify successful Login
        hello_page.verify_success_sign_up()
        self.log.info("User Login")

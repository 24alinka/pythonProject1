import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL


class TestChatMessage:
    log = logging.getLogger("[ChatMessage]")

    @pytest.fixture(scope="function")
    def chat_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield TestChatMessage(driver)
        # Post-conditions
        driver.close()

import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def random_email():
    word = string.ascii_lowercase
    return ''.join(random.choice(word) for x in range(8))


@pytest.fixture(scope="class")
def random_name():
    name = string.ascii_letters
    return ''.join(random.choice(name) for x in range(30))


@pytest.fixture(scope="class")
def random_psw():
    psw = string.ascii_letters + string.digits
    return ''.join(random.choice(psw) for x in range(12))


class TestLoginFrom:
    def test_incorrect_name(self):
        """
        - Create driver
        - Open page
        - Fill user_name
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/User/PycharmProjects/pythonProject1/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Fill UserName
        user_name = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        user_name.send_keys("test test")
        sleep(1)
        # Verify error
        error_element = driver.find_element(by=By.XPATH,
                                            value=".//*[contains(text(), 'Username can only contain letters and numbers.')]")
        assert error_element.text == "Username can only contain letters and numbers.", f"Actual message: {error_element.text}"
        # Close driver
        driver.close()

    def test_incorrect_password(self):
        """
        - Create driver
        - Open page
        - Fill password
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/User/PycharmProjects/pythonProject1/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill password
        pass_name = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        pass_name.send_keys("test123")
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH,
                                            value=".//*[contains(text(), 'Password must be at least 12 characters.')]")
        assert error_element.text == "Password must be at least 12 characters.", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_valid_data(self, random_email, random_name, random_psw):
        """
        - Create driver
        - Open page
        - Fill user_name
        - Fill email
        - Fill password
        - Click on button
        - Successful registration
        """
        # Create driver
        driver = webdriver.Chrome("/Users/User/PycharmProjects/pythonProject1/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill UserName
        user_name = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        user_name.send_keys(random_name)
        sleep(1)

        # Fill email
        user_email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        user_email.send_keys(random_email, "@gmail.com")
        sleep(1)

        # Fill password
        psw_email = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        psw_email.send_keys(random_psw)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Successful registration
        hello_text = driver.find_element(by=By.XPATH, value=".//*[contains(text(),'Hello')]")
        hello_text.is_selected()

        # Close driver
        driver.close()

    def test_invalid_email(self):
        """
        - Create driver
        - Open page
        - Fill user_name
        - Fill email
        - Fill password
        - Click on button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/User/PycharmProjects/pythonProject1/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Fill UserName
        user_name = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        user_name.send_keys("TestAlinkatest")
        sleep(2)

        # Fill email
        user_email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        user_email.send_keys("testalinka-tets@@gmail.com")
        sleep(1)

        # Fill password
        psw_email = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        psw_email.send_keys("testA12345testtest")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH,
                                            value=".//*[contains(text(), 'You must provide a valid email address.')]")
        assert error_element.text == "You must provide a valid email address.", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_same_email(self, random_name, random_psw):
        """
        - Create driver
        - Open page
        - Fill user_name
        - Fill same email
        - Fill password
        - Click on button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome("/Users/User/PycharmProjects/pythonProject1/chromedriver")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Fill UserName
        user_name = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        user_name.send_keys(random_name)
        sleep(1)

        # Fill email
        user_email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        user_email.send_keys("testalinka-tets@gmail.com")
        sleep(1)

        # Fill password
        psw_email = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        psw_email.send_keys(random_psw)
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH,
                                            value=".//*[contains(text(), 'That email is already being used.')]")
        assert error_element.text == "That email is already being used.", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

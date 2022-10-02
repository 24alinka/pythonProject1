import logging

import pytest
<<<<<<< HEAD

from pages.utils import Post
=======
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num
>>>>>>> origin/homework


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

<<<<<<< HEAD
    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)
=======
    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture()
    def hello_page(self, start_page):
        """Sign Up as the user and return the page"""
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        return start_page.sign_up_and_verify(username_value, email_value, password_value)
>>>>>>> origin/homework

    def test_create_post_page(self, hello_page):
        """
        - Pre-conditions:
<<<<<<< HEAD
            - Sign Up/Sign In as a user
=======
            - Sign Up/Sign In as an user
>>>>>>> origin/homework
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
<<<<<<< HEAD
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)
        # Verify the result
        create_post_page.verify_successfully_created()
        self.log.info("The post was sent successfully")

    def test_delete_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
            - Delete post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)
        # Verify the result
        create_post_page.verify_successfully_created()
        # Delete post
        create_post_page.delete_post()
        # Verify the result
        create_post_page.verify_successfully_delete_post()
        self.log.info("Message that post is successfully deleted is appeared")

    def test_edit_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
            - Edit post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)
        # Edit post
        create_post_page.click_edit_post()
        edited_title = "New title"
        edited_body = "New message"
        create_post_page.edit_post(title=edited_title, body=edited_body)
        # Verify the result
        create_post_page.verify_successfully_edit_post()
        self.log.info("The post has been edited")

    def test_create_a_unique_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create unique post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post_with_click_checkbox(post)
        # Verify the result
        create_post_page.verify_successfully_created()
        self.log.info("The post was sent successfully")

    def test_create_a_private_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create private message
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.select(post, select_value="Приватне повідомлення")
        # Verify the result
        create_post_page.verify_private_option()
        self.log.info("The post was sent successfully")

    def test_create_a_group_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create group message
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.select(post, select_value="Групове повідомлення")
        # Verify the result
        create_post_page.verify_group_message_option()
        self.log.info("The post was sent successfully")

    def test_create_all_users_post(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Navigate to create Post Page
            - Create all users message
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.select(post, select_value="Загальнодоступне")
        # Verify the result
        create_post_page.verify_all_users_option()
        self.log.info("The post was sent successfully")
=======
        self.log.info("Moved to Create Post Page")

        # Create Post
        create_post_page.create_post(title=random_str(15), body=random_str(150))
        self.log.info("Post created")

        # Verify the result
        create_post_page.verify_successfully_created()
        self.log.info("Message was verified")
>>>>>>> origin/homework

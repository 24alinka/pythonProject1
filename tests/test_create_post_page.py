import logging

import pytest

from pages.utils import Post


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_create_post_page(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as a user
        - Steps:
            - Navigate to create Post Page
            - Create Post
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

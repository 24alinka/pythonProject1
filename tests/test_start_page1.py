import logging

from pages.utils import User, Post


class TestStartPage:
    log = logging.getLogger("[StartPage]")

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
        # Verify error message
        start_page.verify_email_error2()
        self.log.info("Error was verified")

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

    def test_folowing(self, start_page, random_user):
        """
            - Pre-conditions:
                - Sign up as a user (user1)
                - Create a post
                - Sign Out
                - Sign Up as the other user (user2)
            - Steps:
                - Search  for post by user1
                - Navigate to post
                - Navigate to the user profile
                - Follow the user
                - Navigate to user2 profile
                - Verify following tab
            """
        # Sign Up as a user1
        hello_page = start_page.sign_up_and_verify(random_user)
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post_with_all(
            Post(post.title, post.body, select="Приватне повідомлення", checkbox="yes"))
        # Sign Out
        start_page_return = create_post_page.header.sign_out_click()
        # Sign Up as a User2
        user = User()
        user.fill_data()
        start_page_return.sign_up_and_verify(user)
        # Search  for post by user1
        start_page.header.search_previously_created_post(post, user)

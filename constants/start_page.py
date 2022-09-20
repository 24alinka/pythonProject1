class StartPageConstants:
    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_UP_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # Hints for Sign Up form
    HINT_PASSWORD_XPATH = ".//*[contains(text(), 'Password must be at least 12 characters.')]"
    HINT_PASSWORD_TEXT = "Password must be at least 12 characters."
    HINT_EMAIL_XPATH = ".//*[contains(text(), 'You must provide a valid email address.')]"
    HINT_EMAIL_XPATH2 = ".//*[contains(text(), 'That email is already being used.')]"
    HINT_EMAIL_TEXT = "You must provide a valid email address."
    HINT_EMAIL_TEXT2 = "That email is already being used."
    HINT_EMAIL_ERROR_XPATH = ".//*[contains(text(), 'That email is already being used.')]"
    HINT_EMAIL_ERROR_TEXT = "That email is already being used."
    HINT_NAME_ERROR_XPATH = ".//*[contains(text(), 'Username can only contain letters and numbers.')]"
    HINT_NAME_ERROR_TEXT = "Username can only contain letters and numbers."

    # TODO: this is actually next page
    HELLO_MESSAGE_XPATH = ".//*[contains(text(),'Hello')]"
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"
    HELLO_MESSAGE_TEXT = "Hello {username}, your feed is empty."
class StartPageConstants:
    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_UP_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # Hints for Sign Up
    SIGN_UP_HINT_PASSWORD_XPATH = ".//*[contains(text(), 'Password must be at least 12 characters.')]"
    SIGN_UP_HINT_PASSWORD_TEXT = "Password must be at least 12 characters."
    SIGN_UP_HINT_EMAIL_XPATH = ".//*[contains(text(), 'You must provide a valid email address.')]"
    SIGN_UP_HINT_EMAIL_XPATH2 = ".//*[contains(text(), 'That email is already being used.')]"
    SIGN_UP_HINT_EMAIL_TEXT = "You must provide a valid email address."
    SIGN_UP_HINT_EMAIL_TEXT2 = "That email is already being used."
    SIGN_UP_HINT_EMAIL_ERROR_XPATH = ".//*[contains(text(), 'That email is already being used.')]"
    SIGN_UP_HINT_EMAIL_ERROR_TEXT = "That email is already being used."
    SIGN_UP_HINT_NAME_ERROR_XPATH = ".//*[contains(text(), 'Username can only contain letters and numbers.')]"
    SIGN_UP_HINT_NAME_ERROR_TEXT = "Username can only contain letters and numbers."

    # SIGN IN
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"

    # Hints for Sign In
    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / pasword"

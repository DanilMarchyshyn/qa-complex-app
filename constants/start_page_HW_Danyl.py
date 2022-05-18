class StartPageConstants:
    # Sign In
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Invalid username / pasword"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"

    # Sign Up
    SIGN_UP_USERNAME_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"

    # Register form field
    ERROR_MESSAGE_REGISTER_FORM_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    ERROR_MESSAGE_3_CHARACTERS_TEXT = "Username must be at least 3 characters."
    ERROR_MESSAGE_ONLY_CHARACTERS_NUMBERS_TEXT = "Username can only contain letters and numbers."
    ERROR_MESSAGE_30_CHARACTERS_TEXT = "Username cannot exceed 30 characters."

    # Profile page
    # FixMe: Move to ProfilePage object once created
    SUCCESS_MESSAGE_XPATH = ".//h2"
    SUCCESS_MESSAGE_USERNAME_XPATH = ".//strong"
    SUCCESS_MESSAGE_TEXT = "Hello {username}, your feed is empty."
    SIGN_OUT_BUTTON_XPATH = ".//button[text()='Sign Out']"

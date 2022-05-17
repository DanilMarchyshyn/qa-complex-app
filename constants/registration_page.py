class RegistrationConstants:
    # Register form field
    FILL_USERNAME_XPATH = ".//input[@placeholder='Pick a username']"
    FILL_EMAIL_XPATH = ".//input[@placeholder='you@example.com']"
    FILL_PASSWORD_XPATH = ".//input[@placeholder='Create a password']"
    SIGN_UP_FOR_OA_BUTTON_XPATH = ".//button[text()='Sign up for OurApp']"
    ERROR_MESSAGE_REGISTER_FORM_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    ERROR_MESSAGE_3_CHARACTERS_TEXT = "Username must be at least 3 characters."
    ERROR_MESSAGE_ONLY_CHARACTERS_NUMBERS_TEXT = "Username can only contain letters and numbers."
    ERROR_MESSAGE_30_CHARACTERS_TEXT = "Username cannot exceed 30 characters."

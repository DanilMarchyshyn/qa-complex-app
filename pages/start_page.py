from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, user):
        """Sign in using provided values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    @log_wrapper
    def verify_sign_in_error(self):
        """Verify error on invalid sign in"""
        # error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        error_message = self.wait_until_displayed(xpath=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    @log_wrapper
    def sign_up(self, user):
        """Sign up the user using provided values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @log_wrapper
    def verify_success_sign_up(self, username):
        """Verify hello message for a new user"""
        # hello_message = self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_XPATH)
        hello_message = self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(username=username.lower())
        # assert self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()
        assert self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()

    def input_2symbols_field_username(self, user):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username2sym)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.wait_until_displayed(xpath=self.constants.ERROR_MESSAGE_3_CHARACTERS_TEXT)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def input_empty_field_username(self, user):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.usernameempty)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.wait_until_displayed(xpath=self.constants.ERROR_MESSAGE_3_CHARACTERS_TEXT)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def input_31symbols_field_username(self, user):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username31sym)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def input_space_field_username(self, user):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.usernamespace)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def input_special_symbol_field_username(self, user):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.usernamespecial)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_error_message_3symbols_field_username(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.ERROR_MESSAGE_REGISTER_FORM_XPATH)
        assert error_message.text == self.constants.ERROR_MESSAGE_3_CHARACTERS_TEXT, "Text is not valid"

    def verify_error_message_31symbols_field_username(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.ERROR_MESSAGE_REGISTER_FORM_XPATH)
        assert error_message.text == self.constants.ERROR_MESSAGE_30_CHARACTERS_TEXT, "Text is not valid"

    def verify_error_message_only_characters_field_username(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.ERROR_MESSAGE_REGISTER_FORM_XPATH)
        assert error_message.text == self.constants.ERROR_MESSAGE_ONLY_CHARACTERS_NUMBERS_TEXT, "Text is not valid"

    def verify_success_sign_up(self, username):
        """Verify hello message for a new user"""
        hello_message = self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(username=username.lower())
        assert self.driver.find_element(by=By.XPATH,
                                        value=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()

        # FixMe: Move to ProfilePage object once created
        @log_wrapper
        def logout(self):
            """Sign out from user profile"""
            self.click(self.constants.SIGN_OUT_BUTTON_XPATH)

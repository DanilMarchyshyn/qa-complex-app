from time import sleep

from selenium.webdriver.common.by import By

from constants.registration_page import RegistrationConstants
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = RegistrationConstants()

    def test_fill_2symbols_username(self, username="", email="", password=""):
        """Registration using 2 symbols on field username"""

        # Fill 2 symbols on field username
        self.fill_field(xpath=self.constants.FILL_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.FILL_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.FILL_PASSWORD_XPATH, value=password)
        self.click(xpath=self.constants.SIGN_UP_FOR_OA_BUTTON_XPATH)
        # username_field.send_keys("A1")
        # email = random_symbol("Test", 10) + "@yopmail.com"
        # password_field.send_keys("P@ssw0rdP@ssw0rd")

    def verify_error_using_2symbols_username(self):
        """Verify error message when using 2 symbols on field username"""
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.ERROR_MESSAGE_REGISTER_FORM_XPATH)
        assert error_message.text == self.constants.ERROR_MESSAGE_3_CHARACTERS_TEXT

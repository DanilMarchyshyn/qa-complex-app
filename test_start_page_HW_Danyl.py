import logging
from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page_HW_Danyl import StartPageHwDanyl
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.get(BaseConstants.BASE_URL)
        yield StartPageHwDanyl(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        start_page.sign_up(random_user)
        sleep(1)
        start_page.logout()
        return random_user

    def test_register(self, start_page, random_user):
        """
        - Pre-requirements:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Fill email, login and password fields
        # Click on Sign Up button
        start_page.sign_up(random_user)
        self.log.info("User was registered")
        sleep(1)

        # Verify registration is successful
        start_page.verify_success_sign_up(username=random_user.username)
        self.log.info("Registration for user '%s' was success and verified", random_user.username)

    def test_fill_2symbols_username(self, start_page, random_user):
        start_page.input_2symbols_field_username(random_user)
        start_page.verify_error_message_3symbols_field_username()

    def test_fill_empty_username(self, start_page, random_user):
        start_page.input_empty_field_username(random_user)
        start_page.verify_error_message_3symbols_field_username()

    def test_fill_more_30sym_username(self, start_page, random_user):
        start_page.input_31symbols_field_username(random_user)
        start_page.verify_error_message_31symbols_field_username()

    def test_fill_with_space_username(self, start_page, random_user):
        "A 1"
        start_page.input_space_field_username(random_user)
        start_page.verify_error_message_only_characters_field_username()

    def test_fill_with_special_symbols_username(self, start_page, random_user):
        """!@#$%"""
        start_page.input_special_symbol_field_username(random_user)
        start_page.verify_error_message_only_characters_field_username()

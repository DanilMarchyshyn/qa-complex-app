import logging
import random
import string
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def random_symbol(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    # def test_empty_fields_login(self):
    #     """
    #     - Create driver
    #     - Open start page
    #     - Clear field login
    #     - Clear field password
    #     - Click on 'Sign In' button
    #     - Verify error message
    #     """
    #     # Create driver
    #     driver = WebDriver(executable_path="chromedriver")
    #
    #     # Open start page
    #     self.log.info("Opening start page")
    #     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #
    #     # Clear field login
    #     self.log.info("Cleaning login field")
    #     # - Find element
    #     login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
    #     # - Clear
    #     login_field.clear()
    #
    #     # Clear field password
    #     self.log.info("Cleaning password field")
    #     # - Find element
    #     password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
    #     # - Clear
    #     password_field.clear()
    #
    #     # Click on 'Sign In' button
    #     self.log.info("Going to click 'Sign In' button")
    #     driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()
    #
    #     # Verify error message
    #     self.log.info("Verifying error message")
    #     error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
    #     assert error_message.text == "Error", "Text is not valid"
    #
    #     # Close driver
    #     driver.close()
    #
    # def test_invalid_login(self):
    #     """
    #     - Create driver
    #     - Open start page
    #     - Fill field login
    #     - Fill field password
    #     - Click on 'Sign In' button
    #     - Verify error message
    #     """
    #     # Create driver
    #     driver = WebDriver(executable_path="chromedriver")
    #
    #     # Open start page
    #     self.log.info("Opening start page")
    #     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    #
    #     # Clear field login
    #     self.log.info("Filling login field")
    #     # - Find element
    #     login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
    #     # - Clear
    #     login_field.clear()
    #     # - Fill
    #     login_field.send_keys("RandomName13")
    #     sleep(1)
    #
    #     # Clear field password
    #     self.log.info("Filling password field")
    #     # - Find element
    #     password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
    #     # - Clear
    #     password_field.clear()
    #     # - Fill
    #     password_field.send_keys("RandomPwd11")
    #     sleep(1)
    #
    #     # Click on 'Sign In' button
    #     self.log.info("Going to click 'Sign In' button")
    #     driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()
    #     sleep(1)
    #
    #     # Verify error message
    #     self.log.info("Verifying error message")
    #     error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
    #     assert error_message.text == "Error", "Text is not valid"
    #
    #     # Close driver
    #     driver.close()

    def test_registration(self):
        """
        - Create driver
        - Open start page
        - Fill field new login
        - Fill field new Email
        - Fill field new password
        - Click on 'Sign In' button
        - Verify registration  message
        - Open start page
        - Fill field login on step 3
        - Fill field new password
        - Verify error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field register username
        self.log.info("Filling username field")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        # - Clear
        # username_field.clear()
        # - Fill

        username = random_symbol("TestDM", 20)
        username_field.send_keys(username)
        sleep(1)

        # Clear field register email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        # - Clear
        # email_field.clear()
        # - Fill
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Clear field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        # - Clear
        # password_field.clear()
        # - Fill
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify message
        self.log.info("Verifying  button Sign Out")
        button_name = driver.find_element(by=By.XPATH, value=".//button[text()='Sign Out']")
        assert button_name.text == "Sign Out", "Text is valid"

        # Close driver
        driver.close()

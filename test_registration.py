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

    def test_registration(self):
        """
        - Create driver
        - Open start page
        - Fill field random username
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verify on 'Sign In' button
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill field random username
        self.log.info("Filling username field")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username = random_symbol("TestDM", 20)
        username_field.send_keys(username)
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        #  Verify on 'Sign In' button
        self.log.info("Verifying  button Sign Out")
        button_name = driver.find_element(by=By.XPATH, value=".//button[text()='Sign Out']")
        assert button_name.text == "Sign Out", "Text is valid"

        # Close driver
        driver.close()

    def test_fill_2symbols_username(self):
        """
        - Create driver
        - Open start page
        - Fill 2 symbols on field username
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verifying error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill 2 symbols on field username
        self.log.info("Fill 2 symbols on field username")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_field.send_keys("A1")
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert error_message.text == "Username must be at least 3 characters.", "Text is not valid"

        # Close driver
        driver.close()

    def test_empty_fill_username(self):
        """
        - Create driver
        - Open start page
        - Fill empty field username
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verifying error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill empty field username
        self.log.info("Fill 2 symbols on field username")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_field.clear()
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert error_message.text == "Username must be at least 3 characters.", "Text is not valid"

        # Close driver
        driver.close()

    def test_fill_with_space_username(self):
        """
        - Create driver
        - Open start page
        - Filling symbols and space username field
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verifying error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill empty field username
        self.log.info("Filling symbols and space username field")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_field.send_keys("A 1")
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert error_message.text == "Username can only contain letters and numbers.", "Text is not valid"

        # Close driver
        driver.close()

    def test_fill_more_30sym_username(self):
        """
        - Create driver
        - Open start page
        - Filling 31 symbols username field
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verifying error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill field random 31 symbols username
        self.log.info("Filling 31 symbols username field")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_field.send_keys("username12345678901234567890123")
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert error_message.text == "Username cannot exceed 30 characters.", "Text is not valid"

        # Close driver
        driver.close()

    def test_fill_special_symb_username(self):
        """
        - Create driver
        - Open start page
        - Filling special symbols username field
        - Fill field random Email
        - Fill field  password
        - Click on 'Sign up for OurApp' button
        - Verifying error message
        """

        # Create driver
        driver = WebDriver(executable_path="chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill field random 31 symbols username
        self.log.info("Filling special symbols username field")
        # - Find element
        username_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username_field.send_keys("test!")
        sleep(1)

        # Fill field random Email
        self.log.info("Filling email field")
        # - Find element
        email_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email = random_symbol("Test", 10) + "@yopmail.com"
        email_field.send_keys(email)
        sleep(1)

        # Fill field  password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password_field.send_keys("P@ssw0rdP@ssw0rd")
        sleep(1)

        # Click on 'Sign up for OurApp' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert error_message.text == "Username can only contain letters and numbers.", "Text is not valid"

        # Close driver
        driver.close()

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from utils import random_word, generate_email
import locators


class TestLogin:
    def test_login_by_enter(self, credentials):
        driver = webdriver.Chrome()
        driver.get(data.URL)

        driver.find_element(*locators.ACCOUNT_BUTTON).click()

        self._login(driver, credentials['email'], credentials['password'])

    def test_login_from_registration(self):
        driver = webdriver.Chrome()
        driver.get(data.URL)

        driver.find_element(*locators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.REGISTER_LINK))

        driver.find_element(*locators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.INPUT_NAME))

        name = random_word(6)
        email = generate_email()
        password = data.PASSWORD

        driver.find_element(*locators.INPUT_NAME).send_keys(name)
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTER_BUTTON))

        self._login(driver, email, password)

    def test_login_by_account(self, credentials):
        driver = webdriver.Chrome()
        driver.get(data.URL)

        driver.find_element(*locators.ACCOUNT_LINK).click()

        self._login(driver, credentials['email'], credentials['password'])

    def test_login_from_password_restore(self, credentials):
        driver = webdriver.Chrome()
        driver.get(data.URL)

        driver.find_element(*locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.RESTORE_PASSWORD_LINK
            )
        )
        driver.find_element(*locators.RESTORE_PASSWORD_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.LOGIN_LINK
            )
        )
        driver.find_element(*locators.LOGIN_LINK).click()
        self._login(driver, credentials['email'], credentials['password'])

    @staticmethod
    def _login(driver, email, password):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.MAKE_ORDER_BUTTON
            )
        )

        driver.quit()

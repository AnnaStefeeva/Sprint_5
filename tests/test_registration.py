from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from utils import random_word, generate_email
import locators


class TestRegistration:
    def test_successful_registration(self):
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

        driver.find_element(*locators.INPUT_NAME).send_keys(name)
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTER_BUTTON))

        driver.quit()

    def test_registration_with_incorrect_password(self):
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
        password = '12345'

        driver.find_element(*locators.INPUT_NAME).send_keys(name)
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.INPUT_ERROR_TEXT
            )
        )
        error_text = driver.find_element(*locators.INPUT_ERROR_TEXT).text
        assert error_text == data.INCORRECT_PASSWORD_ERROR_TEXT

        driver.quit()

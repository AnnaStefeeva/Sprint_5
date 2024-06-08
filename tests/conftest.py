from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utils import random_word, generate_email
import data
import locators


@pytest.fixture(scope='session')
def credentials():
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

    driver.quit()

    return {
        'name': name,
        'email': email,
        'password': password
    }

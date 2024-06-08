from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from data import URL


class TestLogOut:
    def test_log_out(self, credentials):
        driver = webdriver.Chrome()
        driver.get(URL)

        driver.find_element(*locators.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.find_element(*locators.INPUT_EMAIL).send_keys(credentials['email'])
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(credentials['password'])
        driver.find_element(*locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.MAKE_ORDER_BUTTON
            )
        )
        driver.find_element(*locators.ACCOUNT_TITLE).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.EXIT_BUTTON
            )
        )

        driver.find_element(*locators.EXIT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.quit()

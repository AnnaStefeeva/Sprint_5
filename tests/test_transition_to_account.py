from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URL
import locators


class TestTransitionToAccount:
    def test_account_button(self):
        driver = webdriver.Chrome()
        driver.get(URL)

        driver.find_element(*locators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.quit()

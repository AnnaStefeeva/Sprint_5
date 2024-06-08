from selenium import webdriver
from data import URL, SELECTED_TAB_CLASS
import locators


class TestTransitionBetweenProduct:
    def test_transition_between_product(self):
        driver = webdriver.Chrome()
        driver.get(URL)

        bun_div = driver.find_element(*locators.BUN_TAB)
        souces_div = driver.find_element(*locators.SOUCES_TAB)
        filling_div = driver.find_element(*locators.FILLINGS_TAB)
        assert SELECTED_TAB_CLASS in bun_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in souces_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in filling_div.get_attribute('class')

        souces_div.click()

        bun_div = driver.find_element(*locators.BUN_TAB)
        souces_div = driver.find_element(*locators.SOUCES_TAB)
        filling_div = driver.find_element(*locators.FILLINGS_TAB)
        assert SELECTED_TAB_CLASS not in bun_div.get_attribute('class')
        assert SELECTED_TAB_CLASS in souces_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in filling_div.get_attribute('class')

        filling_div.click()

        bun_div = driver.find_element(*locators.BUN_TAB)
        souces_div = driver.find_element(*locators.SOUCES_TAB)
        filling_div = driver.find_element(*locators.FILLINGS_TAB)
        assert SELECTED_TAB_CLASS not in bun_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in souces_div.get_attribute('class')
        assert SELECTED_TAB_CLASS in filling_div.get_attribute('class')

        bun_div.click()

        bun_div = driver.find_element(*locators.BUN_TAB)
        souces_div = driver.find_element(*locators.SOUCES_TAB)
        filling_div = driver.find_element(*locators.FILLINGS_TAB)
        assert SELECTED_TAB_CLASS in bun_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in souces_div.get_attribute('class')
        assert SELECTED_TAB_CLASS not in filling_div.get_attribute('class')

        driver.quit()

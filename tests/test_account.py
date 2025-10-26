from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import AccountLocators
from data import Data

class TestAccount:

    def test_open_account_redirect_to_login(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()

        login_header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert login_header.is_displayed()

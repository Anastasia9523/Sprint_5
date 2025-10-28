from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AccountLocators, LoginLocators
from data import Data

class TestLogout:

    def test_logout_from_account(self, driver):
        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_EMAIL)).send_keys(Data.TEST_EMAIL)

        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.LOGOUT_BUTTON)).click()

        login_field = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_EMAIL))

        assert login_field.is_displayed()

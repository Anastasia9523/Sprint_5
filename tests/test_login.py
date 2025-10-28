from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data
from locators import MainPage, LoginLocators, AccountLocators

class TestLogin:

    def test_login_from_main_page(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.LOGIN_BUTTON_MAIN)).click()

        driver.find_element(*LoginLocators.LOGIN_EMAIL).send_keys(Data.TEST_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        account_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.ACCOUNT_BUTTON))
        assert account_button.is_displayed()

    def test_login_from_account_button(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()

        driver.find_element(*LoginLocators.LOGIN_EMAIL).send_keys(Data.TEST_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        account_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.ACCOUNT_BUTTON))
        assert account_button.is_displayed()

    def test_login_from_registration_form(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.LOGIN_BUTTON_MAIN)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Войти"))).click()

        driver.find_element(*LoginLocators.LOGIN_EMAIL).send_keys(Data.TEST_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        account_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.ACCOUNT_BUTTON))
        assert account_button.is_displayed()

    def test_login_from_forgot_password_form(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.LOGIN_BUTTON_MAIN)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Восстановить пароль"))).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Войти"))).click()

        driver.find_element(*LoginLocators.LOGIN_EMAIL).send_keys(Data.TEST_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        account_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.ACCOUNT_BUTTON))
        assert account_button.is_displayed()

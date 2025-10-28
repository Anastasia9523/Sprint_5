from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AccountLocators, LoginLocators, MainPage
from data import Data


class TestConstructorNavigation:

    def test_return_to_constructor_from_account(self, driver):
        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_EMAIL)).send_keys(Data.TEST_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD).send_keys(Data.TEST_PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocators.ENTER_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()


        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON))

        # Переход в конструктор по кнопке "Конструктор" 
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.CONSTRUCTOR_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.ORDER_BUTTON))

        assert driver.current_url == Data.URL

        #  Переход в конструктор по клику на логотип Stellar Burgers 
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON))

        WebDriverWait(driver, 10).until( expected_conditions.element_to_be_clickable(AccountLocators.LOGO_BUTTON)).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.ORDER_BUTTON))

        assert driver.current_url == Data.URL

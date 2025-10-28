from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import MainPage, RegistrationLocators, LoginLocators
from helpers import Helper


class TestRegistration:

    def test_successful_registration(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.LOGIN_BUTTON_MAIN)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        email = Helper.generate_email()
        password = Helper.generate_password(length=8)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(Data.TEST_NAME)

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON)).click()

        enter_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginLocators.ENTER_BUTTON))
        assert enter_button.is_displayed()

    def test_registration_with_short_password(self, driver):

        driver.get(Data.URL)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.LOGIN_BUTTON_MAIN)).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        email = Helper.generate_email()
        short_password = "123"

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(Data.TEST_NAME)

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(short_password)

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON)).click()

        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))
        assert error_message.is_displayed()

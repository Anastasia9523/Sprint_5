from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data
from locators import ConstructorLocators

class TestConstructorSections:

    def test_constructor_tabs(self, driver):
        driver.get(Data.URL)
        wait = WebDriverWait(driver, 10)

        # Булки
        element = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SECTION_BUNS))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        assert wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.CONTENT_BUNS))

        # Соусы
        element = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SECTION_SAUCES))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        assert wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.CONTENT_SAUCES))

        # Начинки
        element = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SECTION_FILLINGS))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        assert wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.CONTENT_FILLINGS))

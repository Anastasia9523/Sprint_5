from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data
from locators import ConstructorLocators

class TestConstructorSections:

    def open_page(self, driver):

        driver.get(Data.URL)
        return WebDriverWait(driver, 10)

    def test_open_buns_tab(self, driver):

        wait = self.open_page(driver)
        buns_tab = wait.until(expected_conditions.presence_of_element_located(ConstructorLocators.SECTION_BUNS))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab) 
        assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class")

    def test_open_sauces_tab(self, driver):

        wait = self.open_page(driver)
        sauces_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SECTION_SAUCES))
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        sauces_tab.click()
        assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class")

    def test_open_fillings_tab(self, driver):

        wait = self.open_page(driver)
        fillings_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SECTION_FILLINGS))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        fillings_tab.click()
        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")
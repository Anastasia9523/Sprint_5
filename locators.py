from selenium.webdriver.common.by import By 

class MainPage: # Главная страница 
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка «Войти в аккаунт» на главной странице 
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

class RegistrationLocators: # Страница регистрации 
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]") # Поле «Имя» 
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]") # Поле «Email» 
    PASSWORD_INPUT = (By.NAME, "Пароль") # Поле «Пароль» 
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка регистрации) 
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(),'Некорректный пароль')]") # Ошибка при коротком пароле

class LoginLocators: # Страница входа 
    LOGIN_EMAIL = (By.NAME, "name") # Поле "Email" 
    LOGIN_PASSWORD = (By.NAME, "Пароль") # Поле "Пароль" 
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка входа в аккаунт 
    
class AccountLocators: # Личный кабинет 
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Кнопка перехода в личный кабинет 
    LOGOUT_BUTTON =  (By.XPATH, "//button[text()='Выход']") # Кнопка выхода 
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка «Конструктор» 
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Логотип Stellar Burgers 
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок "Вход"
    
class ConstructorLocators: # Конструктор 
    SECTION_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab__1SPyG')]") # Раздел "Булки". 
    SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab__1SPyG')]") # Раздел "Соусы".
    SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab__1SPyG')]") # Раздел "Начинки".

    CONTENT_BUNS = (By.XPATH, "//h2[text()='Булки']")
    CONTENT_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    CONTENT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")
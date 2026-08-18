from selenium.webdriver.common.by import By

class LoginPageLocators:

    #Заголовок формы авторизации:
    REGISTER_MAIN_HEADER = (By.XPATH, '//h2[text()="Вход"]')

    #Поля формы авторизации:
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')

    #Кнопка "Войти":
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')
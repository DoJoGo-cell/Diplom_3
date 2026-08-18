import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageObjects
from urls import URLs

class MainPageObjects(BasePageObjects):

    @allure.step('Ожидание загрузки URL главной страницы Stellar Burger')
    def wait_for_load_main_page(self):
        self.wait_load_url(URLs.BASE_URL)

    @allure.step('Ожидание загрузки кнопки перехода на раздел "Лента заказов"')
    def wait_for_load_orders_list_text(self):
        self.wait_element_visability(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step('Нажатие на кнопку перехода на страницу "Лента заказов"')
    def click_button_orders_list(self):
        self.click(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step('Нажатие на ингредиент "Флюоресцентная булка R2-D3"')
    def click_ingredient_bun(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Ожидание появления ингредиента "Флюоресцентная булка R2-D3" на главной странице')
    def wait_for_load_ingredient_bun(self):
        self.wait_element_visability(MainPageLocators.INGREDIENT_BUN)
        return True
    
    @allure.step('Ожидание появления заголовка всплывающего окна "Детали ингредиента"')
    def wait_for_load_ingredient_details_main_header(self):
        self.wait_element_visability(MainPageLocators.INGREDIENT_DETAILS_MAIN_HEADER)
        return True
    
    @allure.step('Ожидание появления кнопки закрытия окна детелей ингредиента')
    def wait_for_load_closing_element(self):
        self.wait_element_visability(MainPageLocators.CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW)

    @allure.step('Ожидание невидимости заголовка всплывающего окна "Детали ингредиента"')
    def wait_for_invisibility_of_details_main_header(self):
        return self.wait_element_invisability(MainPageLocators.INGREDIENT_DETAILS_MAIN_HEADER)

    @allure.step('Нажатие на кнопку закрытия всплывающего окна "Детали ингредиента"')
    def click_close_button_ingredient_details_window(self):
        self.click(MainPageLocators.CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW)

    @allure.step('Добавление ингредиента в конструктор заказа')
    def add_ingredients_into_constructor(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.INGREDIENTS_CONSTRUCTOR)

    @allure.step('Ожидание появления ингредиента в конструкторе')
    def wait_for_load_ingredient_in_constructor(self):
        self.wait_element_visability(MainPageLocators.LIST_OF_ADDED_INGREDIENTS)

    @allure.step('Ожидание появления числового идентификатора заказа')
    def wait_for_load_order_identificator(self):
        self.wait_text_matches(MainPageLocators.ORDER_IDENTIFICATOR, r'^3\d+')

    @allure.step('Нажатие на кнопку закрытия всплывающего окна "Идентификатор заказа"')
    def click_close_button_order_identificator_window(self):
        self.click_js(MainPageLocators.CLOSE_BUTTON_ORDER_IDENTIFICATOR)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Ожидание завершения анимации загрузки')
    def wait_for_ending_animation_of_loading(self):
        return self.wait_element_invisability(MainPageLocators.LOADING_ANIMATION)
    
    @allure.step('Ожидание закрытия модального окна')
    def wait_for_closing_modal_window(self):
        return self.wait_element_invisability(MainPageLocators.MODAL_WINDOW)


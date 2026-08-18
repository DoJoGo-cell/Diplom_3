import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageObjects
from pages.base_page import BasePageObjects
from pages.orders_list_page import OrdersListPageObjects
from pages.login_page import LoginPageObjects
from urls import URLs
from authorization_data import Data

@allure.feature('Проверка основной функциональности')
class TestMainFunctions:
    
    @allure.title('Проверка перехода на раздел "Лента заказов"')
    @allure.description('Тест проверяет переход на раздел "Лента заказов" нажатием на кнопку перехода "Лента заказов" на главной странице сервиса')
    def test_transition_to_orders_list_page(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)
        orders_list_page = OrdersListPageObjects(driver_main_page)

        with allure.step('Переход на страницу "Лента заказов"'):
            main_page.wait_for_load_orders_list_text()
            main_page.click_button_orders_list()
            orders_list_page.wait_for_load_orders_list_page()

        with allure.step('Проверка текущего URL'):
            assert orders_list_page.get_current_url() == URLs.ORDERS_LIST_URL

    @allure.title('Проверка перехода на раздел "Конструктор"')
    @allure.description('Тест проверяет переход на раздел "Конструктор" нажатием на кнопку перехода "Конструктор" на странице "Лента заказов"')
    def test_transition_to_main_page(self, driver_orders_list_page):
        orders_list_page = OrdersListPageObjects(driver_orders_list_page)
        main_page = MainPageObjects(driver_orders_list_page)

        with allure.step('Переход на раздел "Конструктор"'):
            orders_list_page.click_button_constructor()
            main_page.wait_for_load_main_page()

        with allure.step('Проверка текущего URL'):
            assert orders_list_page.get_current_url() == URLs.BASE_URL

    @allure.title('Проверка появления всплывающего окна с деталями при нажатии на ингредиент')
    @allure.description('Тест проверяет появления всплывающего окна с деталями при нажатии на ингредиент(Флюоресцентная булка R2-D3) на главной странице сервиса')
    def test_ingredient_details_window_appearance(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)

        with allure.step('Проверка появления заголовка всплывающего окна "Детали ингредиента" при нажатии на ингредиент'):
            main_page.click_ingredient_bun()
            assert main_page.wait_for_load_ingredient_details_main_header()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    @allure.description('Тест проверяет закрытие всплывающего окна с деталями ингредиента при нажатии на крестик в углу окна')
    def test_ingredient_details_window_closing(self, driver_main_page):
        main_page = MainPageObjects(driver_main_page)

        with allure.step('Открытие всплывающего окна "Детали ингредиента"'):
            main_page.click_ingredient_bun()
            main_page.wait_for_load_ingredient_details_main_header()
            main_page.wait_for_load_closing_element()

        with allure.step('Закрытие всплывающего окна "Детали ингредиента"'):
            main_page.click_close_button_ingredient_details_window()

        with allure.step('Проверка отсутствия всплывающего окна "Детали ингредиента"'):
            assert main_page.wait_for_invisibility_of_details_main_header()

    @allure.title('Проверка увеличения счетчика ингредиента при его добавлении в конструктор')
    @allure.description('Тест проверяет увеличения счетчика ингредиента при его добавлении в конструктор на главной странице сервиса')
    def test_increasing_the_counter_of_ingredients(self, driver_login_page):
        main_page = MainPageObjects(driver_login_page)
        base_page = BasePageObjects(driver_login_page)
        login_page = LoginPageObjects(driver_login_page)

        with allure.step('Авторизация пользователя'):
            login_page.fill_authorization_form(Data.DATA_SET)
            login_page.click_button_authorization()

        with allure.step('Добавление ингредиента в конструктор'):
            main_page.wait_for_load_main_page()
            main_page.wait_for_load_ingredient_bun()
            main_page.add_ingredients_into_constructor()
            main_page.wait_for_load_ingredient_in_constructor()

        with allure.step('Проверка увеличения счетчика'):
            element = base_page.find(MainPageLocators.INGREDIENT_COUNTER)
            text = element.text
            count = int(text)
            assert count > 0


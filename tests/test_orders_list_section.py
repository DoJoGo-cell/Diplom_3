import allure
from locators.orders_list_page_locators import OrdersListPageLocators
from pages.main_page import MainPageObjects
from pages.base_page import BasePageObjects
from pages.orders_list_page import OrdersListPageObjects

@allure.feature('Проверка раздела "Лента заказов"')
class TestOrdersListSection:

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании заказа')
    @allure.description('Тест проверяет увеличение счетчика "Выполнено за всё время" при создании заказа в разделе "Лента заказов"')
    def test_increasing_counter_for_all_time(self, driver_login_page_and_authorization_and_make_order):
        base_page = BasePageObjects(driver_login_page_and_authorization_and_make_order[0])
        main_page = MainPageObjects(driver_login_page_and_authorization_and_make_order[0])
        orders_list_page = OrdersListPageObjects(driver_login_page_and_authorization_and_make_order[0])

        number_for_all_time = driver_login_page_and_authorization_and_make_order[1]

        with allure.step('Проверка информации о заказе в разделе "Лента заказов"'):
            main_page.click_button_orders_list()
            orders_list_page.wait_for_load_orders_list_page()
            orders_list_page.wait_for_load_orders_list_page_header()

        with allure.step('Проверка увеличения счетчика'):
            element = base_page.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME)
            text = int(element.text)
            assert text == (number_for_all_time + 1)

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании заказа')
    @allure.description('Тест проверяет увеличение счетчика "Выполнено за сегодня" при создании заказа в разделе "Лента заказов"')
    def test_increasing_counter_for_today(self, driver_login_page_and_authorization_and_make_order):
        base_page = BasePageObjects(driver_login_page_and_authorization_and_make_order[0])
        main_page = MainPageObjects(driver_login_page_and_authorization_and_make_order[0])
        orders_list_page = OrdersListPageObjects(driver_login_page_and_authorization_and_make_order[0])

        number_for_today = driver_login_page_and_authorization_and_make_order[2]

        with allure.step('Проверка информации о заказе в разделе "Лента заказов"'):
            main_page.click_button_orders_list()
            orders_list_page.wait_for_load_orders_list_page()
            orders_list_page.wait_for_load_orders_list_page_header()

        with allure.step('Проверка увеличения счетчика'):
            element = base_page.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY)
            text = int(element.text)
            assert text == (number_for_today + 1)

    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    @allure.description('Тест проверяет появления номера заказа в разделе "В работе" после оформления заказа')
    def test_number_appearance_in_orders_list_section(self, driver_login_page_and_authorization_and_make_order):
        base_page = BasePageObjects(driver_login_page_and_authorization_and_make_order[0])
        main_page = MainPageObjects(driver_login_page_and_authorization_and_make_order[0])
        orders_list_page = OrdersListPageObjects(driver_login_page_and_authorization_and_make_order[0])

        order_number = driver_login_page_and_authorization_and_make_order[3]

        with allure.step('Проверка информации о заказе в разделе "Лента заказов"'):
            main_page.click_button_orders_list()
            orders_list_page.wait_for_load_orders_list_page()
            orders_list_page.wait_for_load_orders_list_page_header()
            orders_list_page.wait_for_load_number()

        with allure.step('Проверка появления номера заказа'):
            assert (base_page.find(OrdersListPageLocators.ORDER_IDENTIFICATOR).text) == order_number
        
        
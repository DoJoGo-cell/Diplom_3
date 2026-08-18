import allure
from locators.orders_list_page_locators import OrdersListPageLocators
from pages.base_page import BasePageObjects
from urls import URLs

class OrdersListPageObjects(BasePageObjects):

    @allure.step('Нажатие на кнопку перехода на страницу "Конструктор"')
    def click_button_constructor(self):
        self.click(OrdersListPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ожидание загрузки URL страницы "Лента заказов"')
    def wait_for_load_orders_list_page(self):
        self.wait_load_url(URLs.ORDERS_LIST_URL)

    @allure.step('Ожидание загрузки заголовка страницы "Лента заказов"')
    def wait_for_load_orders_list_page_header(self):
        self.wait_element_visability(OrdersListPageLocators.ORDERS_LIST_MAIN_HEADER)

    @allure.step('Ожидание загрузки номера заказа')
    def wait_for_load_number(self):
        self.wait_text_matches(OrdersListPageLocators.ORDER_IDENTIFICATOR, r'\d+')
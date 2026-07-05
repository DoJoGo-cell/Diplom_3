import pytest
from selenium import webdriver
from urls import URLs
from pages.main_page import MainPageObjects
from pages.orders_list_page import OrdersListPageObjects
from pages.login_page import LoginPageObjects
from pages.base_page import BasePageObjects
from authorization_data import Data
from locators.orders_list_page_locators import OrdersListPageLocators
from locators.main_page_locators import MainPageLocators

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):

    driver.get(URLs.BASE_URL)

    main_page = MainPageObjects(driver)
    main_page.wait_for_load_main_page()

    return driver
    
@pytest.fixture(scope="function")
def driver_orders_list_page(driver):
    
    driver.get(URLs.ORDERS_LIST_URL)

    orders_list_page = OrdersListPageObjects(driver)
    orders_list_page.wait_for_load_orders_list_page()

    return driver

@pytest.fixture(scope="function")
def driver_login_page(driver):
    
    driver.get(URLs.LOGIN_URL)

    login_page = LoginPageObjects(driver)
    login_page.wait_for_load_login_page()

    return driver

@pytest.fixture(scope="function")
def driver_login_page_and_authorization(driver_login_page):

    login_page = LoginPageObjects(driver_login_page)
    main_page = MainPageObjects(driver_login_page)
    orders_list_page = OrdersListPageObjects(driver_login_page)
    base_page = BasePageObjects(driver_login_page)

    login_page.fill_authorization_form(Data.DATA_SET)
    login_page.click_button_authorization()

    main_page.wait_for_load_main_page()
    main_page.wait_for_load_ingredient_bun()

    main_page.click_button_orders_list()
    orders_list_page.wait_for_load_orders_list_page()
    orders_list_page.wait_for_load_orders_list_page_header()

    completed_orders_all_time_element = base_page.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_ALL_TIME)
    completed_orders_all_time_number = int(completed_orders_all_time_element.text)

    completed_orders_today_element = base_page.find(OrdersListPageLocators.COMPLETED_ORDERS_FOR_TODAY)
    completed_orders_today_number = int(completed_orders_today_element.text)

    orders_list_page.click_button_constructor()

    return driver_login_page, completed_orders_all_time_number, completed_orders_today_number



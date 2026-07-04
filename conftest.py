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
def driver_main_page(request):
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get(URLs.BASE_URL)

    main_page = MainPageObjects(driver)
    main_page.wait_for_load_main_page

    yield driver
    driver.quit()

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver_orders_list_page(request):
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get(URLs.ORDERS_LIST_URL)

    orders_list_page = OrdersListPageObjects(driver)
    orders_list_page.wait_for_load_orders_list_page

    yield driver
    driver.quit()

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver_login_page(request):
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get(URLs.LOGIN_URL)

    login_page = LoginPageObjects(driver)
    login_page.wait_for_load_login_page()

    yield driver
    driver.quit()

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver_login_page_and_authorization_and_make_order(request):
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get(URLs.LOGIN_URL)

    main_page = MainPageObjects(driver)
    login_page = LoginPageObjects(driver)
    orders_list_page = OrdersListPageObjects(driver)
    base_page = BasePageObjects(driver)

    login_page.wait_for_load_login_page()

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

    main_page.add_ingredients_into_constructor()
    main_page.wait_for_load_ingredient_in_constructor()
    main_page.click_order_button()
    main_page.wait_for_load_order_identificator()

    element = base_page.find(MainPageLocators.ORDER_IDENTIFICATOR)
    order_number = element.text

    main_page.click_close_button_order_identificator_window()
    main_page.wait_for_ending_animation_of_loading()
    main_page.wait_for_closing_modal_window
    main_page.wait_for_load_main_page()
    main_page.wait_for_load_ingredient_bun()

    yield driver, completed_orders_all_time_number, completed_orders_today_number, order_number

    driver.quit()
from selenium.webdriver.common.by import By

class OrdersListPageLocators:

    #Заголовок страницы "Лента заказов":
    ORDERS_LIST_MAIN_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')

    #Кнопка перехода "Конструктор":
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a/p[text()="Конструктор"]')

    #Цифры "Выполнено за все время":
    COMPLETED_ORDERS_FOR_ALL_TIME= (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    #Цифры "Выполнено за сегодня":
    COMPLETED_ORDERS_FOR_TODAY= (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")

    #Числовой идентификатор заказа в разделе "В работе":
    ORDER_IDENTIFICATOR = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    


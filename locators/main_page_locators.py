from selenium.webdriver.common.by import By

class MainPageLocators:

    #Кнопка перехода "Лента заказов":
    BUTTON_ORDERS_LIST = (By.XPATH, '//a/p[text()="Лента Заказов"]')

    #Ингредиент "Флюоресцентная булка R2-D3":
    INGREDIENT_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')

    #Заголовок всплывающего окна "Детали ингредиента":
    INGREDIENT_DETAILS_MAIN_HEADER = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    #Кнопка закрытия всплывающего окна "Детали ингредиента":
    CLOSE_BUTTON_INGREDIENT_DETAILS_WINDOW = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    #Конструктор для ингредиентов:
    INGREDIENTS_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list")]')

    #Счетчик количества добавленного ингредиента:
    INGREDIENT_COUNTER = (By.XPATH, '//p[contains(@class, "counter_counter__num")]')

    #Числовой идентификатор заказа после оформления заказа:
    ORDER_IDENTIFICATOR = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    #Кнопка закрытия всплывающего окна "Идентификатор заказа":
    CLOSE_BUTTON_ORDER_IDENTIFICATOR = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    #Список добавленных ингредиентов в конструктор:
    LIST_OF_ADDED_INGREDIENTS = (By.XPATH, '//span[(@class="constructor-element__price") and text()="988"]')

    #Кнопка оформления заказа:
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    #Анимация зугрузки:
    LOADING_ANIMATION = (By.XPATH, '//img[@alt="loading animation"]')

    #Модальное окно:
    MODAL_WINDOW = (By.XPATH, '//div[@class="Modal_modal_overlay__x2ZCr"]')






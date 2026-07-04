import allure
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageObjects:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Получение элемента: {locator}')
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_element_visability(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание невидимости элемента: {locator}')
    def wait_element_invisability(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Клик по элементу: {locator}')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Переместить элемент в конструктор')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)
    
        self.driver.execute_script("""
        function createDragEvent(type, element, target) {
            const dataTransfer = new DataTransfer();
            const event = new DragEvent(type, {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            return element.dispatchEvent(event);
        }
        
        const source = arguments[0];
        const target = arguments[1];
        
        createDragEvent('dragstart', source, target);
        createDragEvent('drag', source, target);
        createDragEvent('dragenter', target, source);
        createDragEvent('dragover', target, source);
        createDragEvent('drop', target, source);
        createDragEvent('dragend', source, target);
    """, source, target)

    
    @allure.step('Ожидание появления URL ссылки: {url}')
    def wait_load_url(self, url):
        self.wait.until(expected_conditions.url_to_be(url))

    @allure.step('Ожидание появления текста по патерну')
    def wait_text_matches(self, locator, pattern):
        self.wait.until(lambda _: bool(re.search(pattern, self.driver.find_element(*locator).text)))

    @allure.step('Отправка данных {data} в элемент: {locator}')
    def send_text(self, locator, data):
        element = self.find(locator)
        element.clear()
        element.send_keys(data)

    @allure.step('Клик(js) по элементу: {locator}')
    def click_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)


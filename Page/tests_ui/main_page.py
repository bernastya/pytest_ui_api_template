from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page.tests_ui.locators import MainPageLocator
import allure


class MainPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Нажатие на кнопку службы поддержки")
    def button_Support_service(self) -> None:
        """Определение локатора"""
        locator = MainPageLocator.SUPPORT
        """Ожидание появления"""
        support_icon = self.wait.until(EC.presence_of_element_located(locator))
        """Нажатие через JS"""
        self.driver.execute_script(
            "arguments[0].closest('svg, button').click();",
            support_icon
        )

    @allure.step("Открытие списка магазинов")
    def opening_shops(self) -> None:
        """Определение локатора"""
        locator = MainPageLocator.SHOPS
        """Ожидание появления списка"""
        shops = self.wait.until(EC.presence_of_element_located(locator))
        """Нажатие через JS"""
        self.driver.execute_script("arguments[0].click();", shops)

    @allure.step("Нажатие на кнопку 'укажите адрес доставки'")
    def click_address_selector(self) -> None:
        """Ожидание кликабельности"""
        button = self.wait.until(EC.element_to_be_clickable(
                                 MainPageLocator.ADDRESS_BUTTON))
        """Нажатие"""
        button.click()

    @allure.step("Ввод текста '{name}' в поле поиска")
    def input_search_query(self, name: str) -> "MainPage":
        """Ожидание появления поля"""
        search_field = self.wait.until(EC.visibility_of_element_located(
                                       MainPageLocator.SEARCH_INPUT))
        """Очистка поля:"""
        search_field.clear()
        """Ввод текста"""
        search_field.send_keys(name)
        return self

    @allure.step("Нажатие на кнопку поиска")
    def click_search_button(self) -> None:
        """Поиск кнопки"""
        search_btn = self.driver.find_element(*MainPageLocator.SEARCH_BUTTON)
        """Нажатие"""
        search_btn.click()

    @allure.step("Получение текста с кнопки адреса")
    def address_button_text(self) -> str:
        """Определение локатора"""
        locator = MainPageLocator.BUTTON
        """Ожидание появления текста и извлечение"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ввод адреса: {name_address}")
    def input_search_address(self, name_address: str) -> "MainPage":
        locator = MainPageLocator.SEARCH_ADDRESS
        """Поиск поля"""
        field = self.wait.until(EC.element_to_be_clickable(locator))
        """Подготовка поля для ввода текса"""
        field.click()
        field.clear()
        """Имитация печати (Цикл for)"""
        for char in name_address:
            field.send_keys(char)
            time.sleep(0.1)
        return self

    @allure.step("Выбор адреса из списка подсказок: {name}")
    def input_address(self, name: str) -> None:
        """Ожидание появления списка"""
        locator_suggest = MainPageLocator.INPUT_ADDRESS
        """Захват первой подсказки"""
        first_suggestion = self.wait.until(EC.visibility_of_element_located(
                                           locator_suggest))
        """Нажатие через JavaScript"""
        self.driver.execute_script("arguments[0].click();", first_suggestion)

    @allure.step("Нажатие кнопки подтверждения")
    def click_button(self) -> None:
        """Определение цели"""
        locator = MainPageLocator.CLICK_BUTTON
        """Ожидание готовности кнопки"""
        button = self.wait.until(EC.element_to_be_clickable(locator))
        """Нажатие"""
        button.click()

    @allure.step("Клик по первому ресторану в списке")
    def first_restaurant(self) -> "MainPage":
        """ Ожидание «чистого» экрана"""
        self.wait.until_not(EC.presence_of_element_located(
                            MainPageLocator.OVERLAY))
        """Поиск карточки ресторана"""
        element = self.wait.until(EC.visibility_of_element_located(
                                  MainPageLocator.RESTAURANT_SNIPPET))
        """Скролл к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: "
                                   "'center'});", element)
        """Принудительное нажатие"""
        self.driver.execute_script("arguments[0].click();", element)
        return self

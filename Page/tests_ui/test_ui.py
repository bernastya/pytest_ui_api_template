from Page.tests_ui.main_page import MainPage
import os
import allure


@allure.feature("Главная страница")
class TestMain_Page:

    @allure.story("Служба поддержки")
    @allure.title("Проверка открытия чата/окна поддержки")
    def test_support_serviсe(self, browser):
        servise = MainPage(browser)
        servise.button_Support_service()

    @allure.story("Магазины")
    @allure.title("Переход в раздел магазинов")
    def test_shops_opening(self, browser):
        shop = MainPage(browser)
        shop.opening_shops()

    @allure.story("Адрес доставки")
    @allure.title("Открытие окна выбора адреса")
    def test_addres(self, browser):
        address_page = MainPage(browser)
        address_page.click_address_selector()

    @allure.story("Поиск товара")
    @allure.title("Поиск категории товаров: '{query}'")
    def test_search_product(self, browser):
        page = MainPage(browser)
        query = os.getenv("SEARCH_QUERY_UI", "Пицца")
        allure.dynamic.title(f"Поиск категории: {query}")
        page.input_search_query(query).click_search_button()
        with allure.step("Проверка URL или заголовка страницы"):
            assert query.lower() in page.driver.title.lower() or \
                        "search" in page.driver.current_url

    @allure.story("Рестораны")
    @allure.title("Переход на страницу первого ресторана в списке")
    def test_open_first_restaurant(self, settled_page):
        settled_page.first_restaurant()
        with allure.step("Проверка, что совершен переход"
                         " в карточку заведения"):
            assert any(word in settled_page.driver.current_url for word in [
                       "restaurant", "place"])

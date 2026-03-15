import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from Page.tests_ui.main_page import MainPage
import allure

load_dotenv()


@pytest.fixture
def browser():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
        driver.maximize_window()
    url = os.getenv("UI_BASE_URL", "https://market-delivery.yandex.ru")
    with allure.step(f"Переход на главную страницу: {url}"):
        driver.get(url)

    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@pytest.fixture
def settled_page(browser):
    page = MainPage(browser)
    address = os.getenv("TEST_ADDRESS")
    with allure.step(f"Предусловие: Установка тестового адреса '{address}'"):
        page.click_address_selector()
        page.input_search_address(address)
        page.input_address(address)
        page.click_button()
        return page

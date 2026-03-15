import pytest
from .data import MOSCOW_COORDS, DEFAULT_PLACE, SEARCH_QUERY
import allure


@allure.feature("Меню")
@allure.story("Получение списка блюд конкретного заведения")
@allure.title(f"Запрос меню для заведения: {DEFAULT_PLACE}")
def test_menu(api):
    with allure.step("Запрос данных из API"):
        response = api.get_menu(**MOSCOW_COORDS, place_slug=DEFAULT_PLACE)
    with allure.step("Проверка статус-кода 200"):
        assert response.status_code == 200
    with allure.step("Проверка наличия данных корзины в ответе"):
        data = response.json()
        assert "cart" in data, f"Ключ 'cart' отсутствует в ответе: {data}"


@allure.feature("Поиск")
@allure.story('Поиск товаров по текстовому запросу""')
@allure.title(
    "Поиск по тексту: '{search_text}' "
    "(ожидаем {expected_count} результат(ов))"
)
@pytest.mark.parametrize("search_text, expected_count", [
    (SEARCH_QUERY, 1),
    ("", 0)
])
def test_product_search(api, search_text, expected_count):
    with allure.step(f"Отправка API запрос поиска с текстом: '{search_text}'"):
        response = api.search_product(text=search_text, **MOSCOW_COORDS)
    with allure.step("Проверка статус-кода 200"):
        assert response.status_code == 200
    with allure.step("Анализ результатов"):
        data = response.json()
        results = data.get("blocks") or data.get("payload")
        if expected_count > 0:
            assert len(results) > 0, (
                f"Ожидались результаты для поиска '{search_text}'"
            )
        else:
            assert isinstance(results, list)


@allure.feature("Корзина")
@allure.story("Очистка/состояние корзины")
@allure.title("Проверка, что корзина пуста")
def test_check_cart_is_empty(api):
    with allure.step("Запрос содержимого корзины"):
        response = api.get_cart()
    with allure.step("Проверка статус-кода 200"):
        assert response.status_code == 200
    with allure.step("Проверка отсутствия товаров в корзине"):
        assert not response.json().get("items"), (
            "Корзина не пуста, хотя ожидалась пустой"
        )


@allure.feature("Доступность")
@allure.story("Проверка списка ресторанов по координатам")
@allure.title(
    "Поиск ресторанов: {lat}, {lon} "
    "(Ожидаем результат: {should_have_results})"
)
@pytest.mark.parametrize("lat, lon, should_have_results", [
    (MOSCOW_COORDS["lat"], MOSCOW_COORDS["lon"], True),
    (90.0, 0.0, False)
])
def test_restaurants_availability(api, lat, lon, should_have_results):
    with allure.step(f"Запрос списка ресторанов для координат: {lat}, {lon}"):
        response = api.get_restaurants(lat=lat, lon=lon)
    with allure.step("Проверка ответа и наличия блоков"):
        assert response.status_code == 200
        data = response.json()
        blocks = data.get("blocks", [])
        if should_have_results:
            assert len(blocks) > 0, "Рестораны должны быть доступны в Москве"
        else:
            assert len(blocks) == 0, "В океане не должно быть ресторанов"

import os
import requests
from dotenv import load_dotenv
from .data import MOSCOW_COORDS
import allure


load_dotenv()

PARAMS = {"api_version": "v1"}


class Product:

    def __init__(self):
        # Теперь это свойства конкретного экземпляра
        self.BASE_URL = os.getenv("BASE_URL")
        self.HEADERS = {
            "User-Agent": os.getenv("USER_AGENT"),
            "Content-Type": "application/json",
            "x-device-id": os.getenv("DEVICE_ID")
        }
        self.SEARCH_QUERY = os.getenv("SEARCH_QUERY")
        self.PARAMS = PARAMS

    @allure.step("API: Получение меню для заведения {place_slug}")
    def get_menu(self, lon, lat, place_slug):
        url = f"{self.BASE_URL}/eats/v1/cart/v2/full-carts"
        params = {
            "place_slug": place_slug,
            "longitude": lon,
            "latitude": lat,
            "shippingType": "delivery"
        }
        return requests.post(url, params=params, headers=self.HEADERS)

    @allure.step("API: Поиск товара с текстом '{text}'")
    def search_product(self, lon, lat, text=None):
        search_text = text if text is not None else self.SEARCH_QUERY
        url = f"{self.BASE_URL}/eats/v1/full-text-search/v1/search"
        payload = {
            "location": {"longitude": lon, "latitude": lat},
            "text": search_text,
            "region_id": 1
        }
        return requests.post(url, json=payload, headers=self.HEADERS)

    @allure.step(
        "API: Поиск с пустым текстовым запросом "
        "(координаты: {lat}, {lon})")
    def search_product_empty_query(self, lon=None, lat=None):
        lon = lon or MOSCOW_COORDS["lon"]
        lat = lat or MOSCOW_COORDS["lat"]
        return self.search_product(lon=lon, lat=lat, text="")

    def get_cart(self):
        url = f"{self.BASE_URL}/api/{self.PARAMS['api_version']}/cart"
        return requests.get(url, params=self.PARAMS, headers=self.HEADERS)

    def get_restaurants(self, lat, lon):
        url = f"{self.BASE_URL}/eats/v1/full-text-search/v1/search"
        payload = {
            "location": {
                "latitude": lat,
                "longitude": lon
            },
            "text": "",
            "region_id": 1
        }
        return requests.post(url, json=payload, headers=self.HEADERS)

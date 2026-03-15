
import os
from dotenv import load_dotenv


load_dotenv()


MOSCOW_COORDS = {
    "lon": float(os.getenv("MOSCOW_LON", 37.639733)),
    "lat": float(os.getenv("MOSCOW_LAT", 55.750980))
}

DEFAULT_PLACE = os.getenv("DEFAULT_PLACE", "shokoladnica_ksfbx")
SEARCH_QUERY = os.getenv("SEARCH_QUERY", "блины")


TEST_ADDRESS = os.getenv("TEST_ADDRESS", "улица Кошкина, 21")
EXPECTED_ADDRESS_PART = os.getenv("EXPECTED_ADDRESS_PART", "кошкина")

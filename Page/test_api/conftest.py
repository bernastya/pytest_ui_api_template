import pytest
from Page.test_api.product_api import Product


@pytest.fixture
def api():
    return Product()


@pytest.fixture
def moscow_coords():
    return {"lon": 37.639733, "lat": 55.750980}

from selenium.webdriver.common.by import By


class MainPageLocator:
    ADDRESS_BUTTON = (By.XPATH, '//div[@class="r1a8ol1h"]/button')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="Найти"]')
    SUPPORT = (By.CSS_SELECTOR, 'button[aria-label="Служба поддержки"]')
    SHOPS = (By.CSS_SELECTOR, 'button[aria-label="Все Магазины"]')
    SEARCH_BUTTON = (By.XPATH, '//button[contains(., "Найти")]')
    BUTTON = (By.XPATH, '//div[@class="r1a8ol1h"]//span')
    SEARCH_ADDRESS = (By.XPATH,
                      '//input[@data-testid="address-input"]')
    INPUT_ADDRESS = (By.CSS_SELECTOR,
                     '[class*="Suggest-Item"], [role="option"]')
    CLICK_BUTTON = (By.XPATH, '//button[contains(., '
                    '"ОК") or contains(., "OK")]')
    RESTAURANT_SNIPPET = (By.CSS_SELECTOR, '[data-testid="snippet-header"]')
    OVERLAY = (By.CSS_SELECTOR, "[class*='Overlay'], [class*='Modal']")

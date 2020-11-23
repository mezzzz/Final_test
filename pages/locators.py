from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.ID, "add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, '[class="price_color"]')
    MESSAGE_PRICE_BOOK = (By.CSS_SELECTOR,'[class="alertinner "] p strong')


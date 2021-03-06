from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID,"id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.ID, "add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, '[class="price_color"]')
    MESSAGE_PRICE_BOOK = (By.CSS_SELECTOR,'[class="alertinner "] p strong')


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn-group"] [href="/ru/basket/"]')
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    BOOK_SELECTOR = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-block"]')
    USER_ICON = (By.CSS_SELECTOR, '[href="/en-gb/accounts/"]')
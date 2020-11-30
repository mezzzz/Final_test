from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def message_basket_is_empty(self):
        message = self.browser.find_element(*BasePageLocators.MESSAGE_BASKET_IS_EMPTY).text
        assert message == 'Ваша корзина пуста Продолжить покупки', "корзина не пуста"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BOOK_SELECTOR), "existing, but not should be"

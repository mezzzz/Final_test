from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        self.add_to_basket_click()
        self.solve_quiz_and_get_code()
        self.check_price()
        self.check_name()

    def add_to_basket_click(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def check_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_was_added = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text
        assert book_name == book_was_added, 'Book name is not equal book was added'

    def check_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_book_equal = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert price_book == price_book_equal, 'Book price is not equal'

    def guest_can_add_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_NAME), "is present, but not should be"


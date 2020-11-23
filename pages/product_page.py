from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_was_added = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text
        assert book_name == book_was_added, 'Book name is not equal book was added'
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_book_equal = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert price_book == price_book_equal, 'Book price is not equal'
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty.'
        text_in_empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert 'Ваша корзина пуста' in text_in_empty_basket, 'Right text in empty basket is not defined.'
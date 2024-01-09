from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), 'Add to cart button is not presented'
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()
    
    def product_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_CONTENT).text
        notice_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_NOTICE).text
        assert  product_name == notice_name, 'Different name in cart'
        
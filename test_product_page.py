import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.skip
@pytest.mark.parametrize('promo', ('promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                   'promo=offer5', 'promo=offer6', 'promo=offer7', 'promo=offer8', 'promo=offer9'))
def test_guest_can_add_product_to_cart(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.product_added_to_cart()

@pytest.mark.skip
def test_notice_isnt_be(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_notise_is_disappeared(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.success_message_should_be_disappeared()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.success_message_should_be_disappeared()
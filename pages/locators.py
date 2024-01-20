from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'Посмотреть корзину')]")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, '.basket-mini .btn.btn-default_inc')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_REPYT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_FROM_NOTICE = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME_FROM_CONTENT = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_CART_NOTICE = (By.CSS_SELECTOR, '.alertinner')

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
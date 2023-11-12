import unittest
from selenium import webdriver
from pages_.logInPage import LogInPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage


class CartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def log_in_functionality(self):
        loginPageObject = LogInPage(self.driver)
        loginPageObject.fill_username_field("lineclean6@gmail.com")
        loginPageObject.click_to_continue_button()
        loginPageObject.fill_password_field("Amazon0.")
        loginPageObject.click_to_signin_button()

    def navigation_bar_functionality(self):
        navigationBarObject = NavigationBar(self.driver)
        navigationBarObject.click_to_cart_button()

    def test_DeletingItemsFromCart(self):
        self.log_in_functionality()
        self.navigation_bar_functionality()
        cartPageObject = CartPage(self.driver)
        cartPageObject.delete_first_item_from_cart()

    def test_SelectingAllItemsInCart(self):
        self.log_in_functionality()
        self.navigation_bar_functionality()
        cartPageObject = CartPage(self.driver)
        cartPageObject.select_all_items_in_cart()

    def test_DeselectAllItemsInCart(self):
        self.log_in_functionality()
        self.navigation_bar_functionality()
        cartPageObject = CartPage(self.driver)
        cartPageObject.deselect_all_items_in_cart()

    def tearDown(self):
        self.driver.close()

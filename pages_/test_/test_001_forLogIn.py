import unittest
from selenium import webdriver
from pages_.logInPage import LogInPage


class LogInTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positiveLogIn(self):
        loginPageObject = LogInPage(self.driver)
        loginPageObject.fill_username_field("lineclean6@gmail.com")
        loginPageObject.click_to_continue_button()
        loginPageObject.fill_password_field("Amazon0.")
        loginPageObject.click_to_signin_button()

        self.assertNotEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_negativeLogIn(self):
        loginPageObject = LogInPage(self.driver)
        loginPageObject.fill_username_field("lineclean6@gmail.com")
        loginPageObject.click_to_continue_button()
        loginPageObject.fill_password_field("12121212")
        loginPageObject.click_to_signin_button()

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_LoginWithForgottenPassword(self):
        loginPageObject = LogInPage(self.driver)
        loginPageObject.fill_username_field("lineclean6@gmail.com")
        loginPageObject.click_to_continue_button()
        loginPageObject.click_to_forgot_your_password_button()
        loginPageObject.click_to_continue_button()

        self.assertNotEqual("Amazon Password Assistance", self.driver.title)

    def tearDown(self):
        self.driver.close()

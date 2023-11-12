from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage


class LogInPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super(LogInPage, self).__init__(driver)
        self.__usernameFieldLocator = (By.ID, 'ap_email')
        self.__continueButtonLocator = (By.ID, 'continue')
        self.__passwordFieldLocator = (By.ID, 'ap_password')
        self.__signInButtonLocator = (By.ID, 'signInSubmit')
        self.__forgotYourPasswordButtonLocator = (By.ID, 'auth-fpp-link-bottom')

    def fill_username_field(self, username):
        userNameFildElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFildElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFildElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFildElement, password)

    def click_to_signin_button(self):
        sleep(6)
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click(signInButtonElement)
        sleep(6)

    def click_to_forgot_your_password_button(self):
        forgotYourPasswordButtonElement = self._find_element(self.__forgotYourPasswordButtonLocator)
        self._click(forgotYourPasswordButtonElement)

from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super(NavigationBar, self).__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__changeLanguageButtonLocator = (By.ID, "icp-nav-flyout")
        self.__chooseLanguageRadioButtonLocator = (By.ID, "icp-language-translation-hint")

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        cartButtonElement.click()

    def click_to_change_language_button(self):
        changeLanguageButton = self._find_element(self.__changeLanguageButtonLocator)
        changeLanguageButton.click()

    def change_random_language(self):
        chooseLanguageRadioButton = self._find_element(self.__chooseLanguageRadioButtonLocator)
        chooseLanguageRadioButton.click()

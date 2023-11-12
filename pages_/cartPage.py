from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from time import sleep


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__firstItemDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
        self.__selectAllItemsButtonLocator = (By.ID, "select-all")
        self.__deselectAllItemsButtonElement = (By.ID, "deselect-all")

    def delete_first_item_from_cart(self):
        firstItemDeleteButtonElement = self._find_element(self.__firstItemDeleteButtonLocator)
        firstItemDeleteButtonElement.click()

    def select_all_items_in_cart(self):
        selectAllItemsButtonElement = self._find_element(self.__selectAllItemsButtonLocator)
        selectAllItemsButtonElement.click()
        sleep(6)

    def deselect_all_items_in_cart(self):
        deselectAllItemsButtonElement = self._find_element(self.__deselectAllItemsButtonElement)
        deselectAllItemsButtonElement.click()
        sleep(6)


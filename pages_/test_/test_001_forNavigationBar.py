import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from time import sleep


class NavigationBarFunctionalityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

    def test_change_language_functionality(self):
        navigationBarObject = NavigationBar(self.driver)
        navigationBarObject.click_to_change_language_button()
        sleep(5)

        self.assertEqual("Change Language & Currency Settings", self.driver.title)

    def test_change_random_language(self):
        self.test_change_language_functionality()
        navigationBarObject = NavigationBar(self.driver)
        navigationBarObject.change_random_language()
        sleep(5)

    def tearDown(self):
        self.driver.close()


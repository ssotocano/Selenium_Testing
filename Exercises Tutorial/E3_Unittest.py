import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class func_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Lab\Selenium-Python\Python Course\Selenium_Drivers\chromedriver\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", driver.title)
        element = driver.find_element_by_id("search_query_top")
        element.send_keys("Selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "Item not found: " not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


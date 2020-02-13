from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"E:\Lab\Selenium-Python\Python Course\Selenium_Drivers\chromedriver\chromedriver.exe")
driver.get("http://automationpractice.com/index.php?controller=authentication")

user = driver.find_element_by_id("email")
user.send_keys("demos@grupofasok.com")
user.send_keys(Keys.TAB)

passwd = driver.find_element_by_id("passwd")
passwd.send_keys("Demos123*")
passwd.send_keys(Keys.ENTER)



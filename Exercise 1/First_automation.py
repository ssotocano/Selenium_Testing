from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\Lab\Selenium-Python\Python Course\Selenium_Drivers\chromedriver\chromedriver.exe")
driver.get("https://python.org")
driver.close()
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"F:\Testing\Selenium_Testing\Selenium_Drivers\chromedriver\chromedriver.exe")
driver.get("https://python.org")
driver.close()
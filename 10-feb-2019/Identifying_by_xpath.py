from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.find_element_by_name("email").send_keys("qspiders")
driver.find_element_by_name("pass").send_keys("automation")
driver.find_element_by_xpath("//a[contains(text(),'Forgotten account?')]").click()




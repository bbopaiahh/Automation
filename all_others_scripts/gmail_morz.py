import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/geckodriver.exe')
driver.get("https://accounts.google.com/")
time.sleep(5)
driver.find_element_by_id("identifierId").send_keys("bpbbopaiahh@gmail.com")
time.sleep(5)
driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_name('password').send_keys('bpbbopaiahh20274516987')
time.sleep(5)
driver.find_element_by_id('passwordNext').click()
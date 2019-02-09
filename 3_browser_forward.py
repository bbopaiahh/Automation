import time

from selenium import webdriver

browser='firefox'

if browser=='firefox':
    driver=webdriver.Firefox(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/geckodriver.exe')
elif browser=='chrome':
    driver=webdriver.Chrome(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/chromedriver.exe')
elif browser=='ie':
    driver=webdriver.Ie(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/IEDriverServer.exe')
else:
    print("Provide appropiate browser name")

driver.get('https://www.makemytrip.com')
time.sleep(5)
driver.find_element_by_id('header_tab_hotels').click()
driver.back()
time.sleep(5)
driver.forward()
driver.find_element_by_id('header_tab_holidays').click()
from selenium import webdriver
import time
driver=webdriver.Ie(executable_path='C:/Users/Lenovo/PycharmProjects/Automation/drivers/IEDriverServer.exe')
driver.get("https://www.facebook.com/")
time.sleep(15)
driver.find_element_by_id("u_0_q").send_keys("qspiders")
time.sleep(5)
driver.find_element_by_id("u_0_s").send_keys("automation")
time.sleep(5)
driver.find_element_by_id("u_0_v").send_keys("9845198451")
time.sleep(5)
driver.find_element_by_id("u_0_12").send_keys("46465454546")
time.sleep(5)
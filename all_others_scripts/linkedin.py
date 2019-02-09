import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Users\Lenovo\PycharmProjects\Automation\browserexe\chromedriver.exe")
driver.get("https://in.linkedin.com/")
time.sleep(5)
driver.find_element_by_name("firstName").send_keys("bbopaiahh")
time.sleep(5)
driver.find_element_by_name("lastName").send_keys("bp")
time.sleep(5)
driver.find_element_by_id("reg-email").send_keys("yahoo@gmail.com")
time.sleep(5)
driver.find_element_by_name("session_password").send_keys("yahoo")


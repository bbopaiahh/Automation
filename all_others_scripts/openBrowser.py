import time
from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:/Users/Lenovo/PycharmProjects/Automation/chromedriver.exe")
#river.get("https://www.google.com/")
driver.get("file:///C:/Users/Lenovo/Desktop/csspage.html")
driver.find_element_by_name("email").send_keys("yahoo@gmail.com")
time.sleep(2)
driver.find_element_by_name("psw").send_keys("info123")
time.sleep(2)
driver.find_element_by_name("psw-repeat").send_keys("info123")
time.sleep(2)
driver.find_element_by_class_name("signupbtn").click()
time.sleep(2)
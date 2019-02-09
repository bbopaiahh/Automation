import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(executable_path='C:\Users\Lenovo\PycharmProjects\Automation\browserexe\chromedriver.exe')
driver.get("https://my.monsterindia.com/create_account.html")
driver.find_element_by_name("firstName").send_keys("bbopaiahh")
time.sleep(5)
driver.find_element_by_name("lastName").send_keys("qspiders")
time.sleep(5)
driver.find_element_by_name("email").send_keys("qspiders@google.com")
time.sleep(5)
driver.find_element_by_id("passwd_id").send_keys("qspiders")
time.sleep(5)
driver.find_element_by_id("mobile2").send_keys("9845198451")
time.sleep(5)
driver.find_element_by_name("keySkills").send_keys("testing")

#sel = Select(driver.find_element_by_class_name('select2-input'))
#select.select_by_visible_text('Chennai')
#sel.select_by_value('1')

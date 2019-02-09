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

driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.find_element_by_id('email').send_keys('7676906699')
driver.find_element_by_id('password').send_keys('pass')
driver.find_element_by_id('u_0_8').click()
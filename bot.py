from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("") # link here

"""
example:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("www.example.com")

acc = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
acc.clear()
acc.send_keys("test")

password = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
password.clear()
password.send_keys("test")

sex = driver.find_element("xpath", '//*[@id="i13"]/div[3]')
sex.click()

value = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]')
value.click()

mail = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
mail.clear()
mail.send_keys("test")

phonenumber = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
phonenumber.clear()
phonenumber.send_keys("test")

text = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')
text.clear()
text.send_keys("test")

driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
"""

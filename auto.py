from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(0.5)
driver.get("https://www.google.com/")
m= driver.find_element("name", "q")
m.send_keys("Tutorialspoint")
time.sleep(0.2)
m.send_keys(Keys.ENTER)

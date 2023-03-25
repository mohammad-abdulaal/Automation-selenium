
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get("https://jonathannorth.com/contact-me/?_ga=2.246653188.1401377910.1675944663-1914739874.1675944663&_gl=1*4cr7xn*_ga*MTkxNDczOTg3NC4xNjc1OTQ0NjYz*_ga_27539YEJKP*MTY3NTk0NDY2Mi4xLjAuMTY3NTk0NDY2Mi4wLjAuMA..")
print("Starting Driver")
time.sleep(1)
Select_box_name=driver.find_element(By.NAME,"your-name")
Select_box_name.click()
time.sleep(1)
Select_box_name.send_keys("Mohammad")

Select_box_email=driver.find_element(By.NAME,"your-email")
Select_box_email.click()
time.sleep(1)
Select_box_email.send_keys("safdanger@live.com")

Select_box_Subject=driver.find_element(By.NAME,"your-subject")
Select_box_Subject.click()
time.sleep(1)
Select_box_Subject.send_keys("blablablablbalbalb")

Select_box_message=driver.find_element(By.NAME,"your-message")
Select_box_message.click()
time.sleep(1)
Select_box_message.send_keys("test")

driver.find_element(By.CLASS_NAME,"wpcf7-submit").click()
time.sleep(1)
print("done ! ")


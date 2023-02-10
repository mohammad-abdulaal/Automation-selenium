from selenium import webdriver
from selenium.webdriver.common.by import By

def test_setup():
    # we put global driver to be readden in all functions    
    global driver
    driver=webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():  
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.implicitly_wait(50)
    driver.find_element(By.TAG_NAME, "button").click()
    x=driver.title
    assert x =='abc'

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")

# to run test we put directorty on the folder and we put pytest test_sample.py
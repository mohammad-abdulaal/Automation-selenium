from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(50)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(50)
driver.maximize_window()
driver.implicitly_wait(40)
source_element=driver.find_element(By.ID,"box6")

target_element=driver.find_element(By.ID,"box106")

actions=ActionChains(driver)

driver.implicitly_wait(50)



actions.drag_and_drop(source_element,target_element).perform()

driver.implicitly_wait(50)
driver.close()
print("Done !")
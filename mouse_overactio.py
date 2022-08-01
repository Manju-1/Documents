from argparse import Action
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver= Chrome("./chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
sleep(5)

admin=driver.find_element(By.XPATH,"//a[@id='menu_admin_viewAdminModule']").click()
usermgt=driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']").click()
users=driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']").click()
act=ActionChains(driver)
sleep(5)
act.move_to_element(admin)
act.move_to_element(usermgt)
act.move_to_element(users).click().perform()


from time import sleep

from selenium.webdriver import Chrome

driver = Chrome("./chromedriver.exe")
driver.get("file:///I:/CSV%20files/demo-html-20220706T062548Z-001/demo-html/demo.html")
sleep(2)
driver.f
sleep(2)
# print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
sleep(1)
driver.find_element_by_id("delete").click()
driver.switch_to.alert.dismiss()
sleep(1)

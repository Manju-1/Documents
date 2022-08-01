from re import findall
from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver import chrome

driver=Chrome("./chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(10)
driver.find_element_by_id("//span[text()='Upload Resume']").click()
sleep(10)
d=findall(r"hello", "hello worl")



driver.find_element_by_id(r"C:\Users\Manju Nath\Desktop\API.tokens.txt").click()

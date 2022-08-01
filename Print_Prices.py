import csv
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver= Chrome("./chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[text()='Twitter']").click()
driver.implicitly_wait(5)
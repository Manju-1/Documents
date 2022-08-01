from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver= Chrome("./chromedriver.exe")
driver.get("file:///I:/CSV%20files/demo-html-20220706T062548Z-001/demo-html/demo.html")
driver.maximize_window()
a=driver.find_element_by_id("standard_cars")
s=Select(a)
s.select_by_visible_text("Mercedes")
sleep(1)
s.select_by_index(5)
sleep(1)
s.select_by_visible_text("toy")
sleep(1)
s.select_by_index(2)
sleep(1)
s.select_by_value("hda")



from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.monsterindia.com/")
a_obj=ActionChains(driver)
driver.maximize_window()


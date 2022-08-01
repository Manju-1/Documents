from selenium.webdriver import Chrome
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome
driver=Chrome("./chromedriver.exe")
driver.get("https://www.monsterindia.com/")
a_obj=ActionChains(driver)
driver.maximize_window()
#class name, tag name, link text
ele=driver.find_element("xpath",'//a[text="Job search"]')
#if want action class methods just type like a_obj.
a_obj.move_to_element(ele).perform()
ele2=driver.find_element("xpath",'//a[text()="jobs by Title"]')
a_obj.move_to_element(ele2).perform()

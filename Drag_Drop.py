from re import A
from  selenium.webdriver import Chrome
from selenium.webdriver.common import action_chains
from selenium.webdriver import ActionChains
from time import sleep
driver=Chrome("./chromedriver.exe")
driver.get("https://www.snapdeal.com/search?clickSrc=top_searches&keyword=shoes&categoryId=0&vertical=p&noOfResults=20&SRPID=topsearch&sort=rlvncy")
driver.implicitly_wait(10)
driver.maximize_window()
element1=driver.find_element_by_xpath("price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded")

element2=driver.find_element_by_xpath("//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# sleep(10)
# ActionChains(driver).drag_and_drop_by_offset(element1, 20, 0).perform()
# sleep(10)
ActionChains(driver).drag_and_drop_by_offset(element2, -80 ,0).perform()
sleep(10)
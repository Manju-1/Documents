from selenium.webdriver import Chrome

from selenium.webdriver import chrome
driver=Chrome("./chromedriver.exe")
driver.get("https://website.informer.com/")
driver.maximize_window()
driver.switch_to_.frame("frame1")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//a[text()="Register"]').click()
driver.switch_to.default_content()
driver.switch_to.frame("FR2")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//img')
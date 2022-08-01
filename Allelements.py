from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver= Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")
d= driver.title
if (d.__eq__(d)):
    print("pass")
else:
    print("fial")

driver.close()
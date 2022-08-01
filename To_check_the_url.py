from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver= Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")
url=driver.current_url
print(url)
if(url.__contains__("google.com")):
    print("pass")
else:
    print("fail")
driver.close()



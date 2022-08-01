from selenium.webdriver  import Chrome
from selenium.webdriver import chrome
driver=Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")
html =driver.page_source
print(html)

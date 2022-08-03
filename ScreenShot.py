from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get("https://www.google.com")
driver.implicitly_wait(10)
driver.get_screenshot_as_file(".\\demo-html.png")
driver.sc

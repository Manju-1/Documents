from selenium.webdriver import Chrome
driver=Chrome("./chromedriver.exe")
driver.get("https://www.facebook.com/")
logo=driver.find_element_by_id("//img[@class='fb_logo _8ilh img']")
if(logo==True):
    print("logo is displayed")
else:
    print("logo is not displayed")
driver.close()
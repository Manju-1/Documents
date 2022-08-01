from webbrowser import Chrome

# Cookies in selenium python
# A cookie is a piece of information from the website and saved by your web browser
# Cookies are a way of remembering users and their interaction with the site by storing information in the cookie file as key-value pairs.
# It stores the login information like user name/email and password
# An HTTP cookie is also known as a web cookie, a browser cookie or an Internet cookie.
# One website cannot access the cookies set by other websites
#
# Each cookie is associated with a name, value, domain, path, termination, and status of whether it is safe or not. We validate the cookie using selenium; selenium can parse all the cookies
# When testing a web application using the Selenium, you may need to create, update, or delete a cookie to check the behavior of the website with and without cookies.
# For example, when you automate e-commerce sites, you will set cookies for logins, products added to carts using cookies and the product you visited in or searched in past days.
#
# Get
# Cookies in python
# get_cookies() used to return the list of all cookies stored in the web browser.
# # Go to the correct domain
# driver.get("https://www.example.com")
# # And now output all the available cookies for the current URL
# driver.get_cookies()
#
# Get Cookie by name in python selenium
# get_cookie() used to return the specific cookie according to its name.
# driver.get_cookie('foo')
#
# Add Cookie in python selenium
# add_cookie() method is used to create and add the cookie.
# # Go to the correct domain
# driver.get("https://chercher.tech")
# # Now set the cookie. This one's valid for the entire domain
# cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
# driver.add_cookie(cookie)
#
# Delete Cookie in python
# Using delete_cookie() to delete a cookie according to its name.
# driver.delete_cookie("foo")
#
# Delete All Cookie in python selenium
# delete_all_cookies() is used to delete all cookies.
#
# driver.delete_all_cookies()
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver= Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")
x=driver.get_cookies()
# print(x)
s=driver.get_cookie('foo')
# print(s)
a=driver.add_cookie("manju")
print(a)
driver.maximize_window()
driver.close()
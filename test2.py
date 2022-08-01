from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
driver= Chrome("./chromedriver.exe")
driver.get("file:///I:/CSV%20files/demo-html-20220706T062548Z-001/demo-html/demo.html")
driver.maximize_window()
box=driver.find_element_by_id("standard_cars")
s=Select(box)
all_options=s.options
# items=[]
# for item in all_options:
#     items.append(item.text)
#
items=[item.text for item in all_options]
s.select_by_visible_text(items[-1])
s.select_by_visible_text(items[0])

for item in items:
    s.select_by_visible_text(item)
#
# for item in items[::-1]:
#     s.select_by_visible_text(item)



car="Mercedes"
for item in items:
    if item==car:
        s.select_by_visible_text(car)

for index, item in enumerate(items):
    if item==car:
        s.select_by_visible_text(car)
        print(f"index of {car} is {index}")


s.select_by_visible_text("Mercedes")
sleep(2)

current_selected_option=s.first_selected_option
print(current_selected_option.text)





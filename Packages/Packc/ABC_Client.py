import sys
sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\packA")
sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\packB")
sys.path.append(r"(C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\packB\Stu.py)")
import Emp
obj=Emp.Employee(101,"manju",150000)
obj.display_Emp()


import Stu
obj=Stu.Student(11,"scott", 'B')
obj.display_stu()
#Approach-2
from Emp import  Employee
obj=Employee(102,"heloo", 250000)
obj.display_Emp()

from Stu import Sutednt
obj=Sutednt(104,"Mani", "A")
obj.display_stu


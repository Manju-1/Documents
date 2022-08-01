import sys
#Approach-1
#take the path of pack1
#take the path of pack2
# sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\pack1")
# sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\pack2")
# import Module1
# import Module2
# Module1.display()
# Module2.show()

# #Approach-2
import sys
sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\pack1")
sys.path.append(r"C:\Users\Manju Nath\PycharmProjects\selenium_project\Packages\pack2")
from Module1 import *
from Module2 import *
display()
show()
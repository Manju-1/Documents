#inheritance: Aquaring all the attributes (variables) and behavior(methods)
# from one class to another calss is called inheritance
#Objective of inheritance:
  #1.code re-usability
  #2.Avoid duplication

#Types of inheritance:
 #1.Single level inheritance
 #2. multi level inheritnace
 #3.Heirachical inheritance
 #4.Multiple inheritance
class A:
     def m1(self):
         print("this is m1 method from class A")
class B(A):
    def m2(self):
        print("this is method from class B")
b=B()
b.m2()  #this is method from class B
b.m1()  #this is m1 method from class A
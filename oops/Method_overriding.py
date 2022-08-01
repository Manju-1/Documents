class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1() # this call the parent class through child class

obj=B()
obj.m1()
#this is m1 method from class B
# this is m1 method from class A
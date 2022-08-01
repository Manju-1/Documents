class A:
    a,b=10,20


class B(A):
    i,j=100,200
    def m1(self,x,y):
        print(x+y)           #3000
        print(self.i+self.j) #300
        print(self.a+self.b) #30
obj=B()
obj.m1(1000,2000)
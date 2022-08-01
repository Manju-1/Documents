class A:
    x,y=10,20
    def add(self):
        print(self.a+self.b)#30

class B(A):
    a,b=10,20
    def mul(self):
        print(self.a*self.b)#200

class C(B):
    i,j=50,30
    def sub(self):
        print(self.a-self.b)#-10 this is the "A" class value we can access parent class variable with help
                            # of self keyword
        print(self.i-self.j)#20

obj=C()
obj.sub()
obj.mul()
obj.add()


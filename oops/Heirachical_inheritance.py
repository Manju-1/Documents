class A:
    x,y=10,20
    def add(self):
        print(self.x+self.y)

class B(A):
    a,b=10,20
    def mul(self):
        print(self.a*self.b)

class C(A):
    i,j=200,100
    def sub(self):
        print(self.i-self.j)

obj=B()
obj.mul()#200
obj.add()#30

obj=C()
obj.sub()#100
obj.add()#30
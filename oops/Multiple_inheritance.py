class A:
    x,y=10,20
    def add(self):
        print(self.x+self.y)
class B:
    x,y=10,20
    def mul(self):
        print(self.x*self.y)

class C(A,B):
    i,j=200,1000
    def sub(self):
        print(self.i-self.j)

obj=C()
obj.sub()
obj.mul()
obj.add()

#python suport the multiple inheritance but java not suport

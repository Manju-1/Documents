class A:
    x,y=10,20
    def add(self):
        print(self.x + self.y)
class B(A):
    a,b=200,100
    def sub(self):
        print(self.a - self.b)
obj=B()
obj.add() #30
obj.sub() #100
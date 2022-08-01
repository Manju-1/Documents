#polymorphism we can implement using overloading concept..(polymorphism)
class Human:
    def sayhello(self, name=None): #default value
        if name is not None:
            print("Hello" +name)
        else:
            print("hello")
h=Human()
h.sayhello()# without parameter
h.sayhello("scott")


# example2

class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

obj=Calculation()
# one method having multiple function is called method overloading or polymorshism
obj.add()#0
obj.add(10,20)#30
obj.add(10,20,30)#60
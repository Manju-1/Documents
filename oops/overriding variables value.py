class Parent:
    name="scott"

class Child(Parent):
    name = "john"  #overriding the variablee value
    # if you want access parent variable create one  one method like below
    # def parent_variable_value(self):
    #     print(super().name)

obj=Child()
print(obj.name) # here overriding the value of parent class
# obj.parent_variable_value()
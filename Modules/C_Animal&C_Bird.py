# Approach-1
import C_Animal
import C_Bird
obj=C_Animal.Animal()
obj.display()


obj=C_Bird.Brid()
obj.display()
#Approach-2
from C_Animal import  Animal
from  C_Bird import  Brid
obj=Animal()
obj.display()

obj=Brid()
obj.display()

#we can access two classes function into one moudle
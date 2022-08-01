
#How to call the Two function  throgh one module like(Aimal&Bird_Module) only when function name same in two moudle
#Approch-1
import Animal
import  Bird
Animal.fly()
Animal.color()

Bird.fly()
Bird.color()


#Approch-2
from Animal import *
fly()
color()
from Bird import *
fly()
color()
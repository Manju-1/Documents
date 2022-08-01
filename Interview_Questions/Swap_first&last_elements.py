input=[12,35,9,56,24]
input1=[12,35,9,56,24]
output=[24,35,9,56,12]

#Approach-1
def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return  newlist
print(swaplist(input))

#approch-2
#using unpacking
def swaplist(list):
    get = list[-1],list[0]
    list[0],list[-1] = get
    return list
print (swaplist(input1))

#Approach-3
input2=[12,35,9,56,24]
def swaplist(list):
    start, *middle, end= list
    list= [end,*middle,start]
    return  list
print(swaplist(input2))
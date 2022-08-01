class Emp:
    def __init__(self, eid, ename, sal):
        self.ename=ename
        self.eid=eid
        self.sal=sal
    def __str__(self): # this string constructor this return only string values
        print(self.ename)

    def display(self): # this is method
        print(self.ename, self.sal,self.eid)

e1=Emp(101, "steve", 1000)
# print(e1)
e1.display() #steve 1000 101 1000 101
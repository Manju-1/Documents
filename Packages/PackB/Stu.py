class Student:
    def __init__(self,sid,sname,grad):
        self.sid=sid
        self.sname=sname
        self.grad=grad
    def display_stu(self):
        print(self.sid, self.sname, self.grad)
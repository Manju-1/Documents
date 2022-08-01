class Bank:
    def rate_of_interest(self):
        return 0       # rate of interest is 0

class XBank(Bank):
    def rate_of_interest(self):
        return 10      #  XBank rate of interest is 10

class YBank(Bank):
    def rate_of_interest(self):
        return 12      #YBank rate of interest is 12

obj=XBank()
print(obj.rate_of_interest())#10

obj=YBank()
print(obj.rate_of_interest())#12

# this is also heirachical inheritance
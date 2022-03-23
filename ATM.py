class Atm():
    def __init__(self,pincode,username,cardnumber,pinnumber):
        self.pincode=pincode
        self.username=username
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def Cash(self):
        print("Cashed With Drawl")    
    def BalanceInquire(self):
        print("Checking Balance")
    def language(self):
        print("English,Hindi")    

atharvatm=Atm("1234","atharv123",12345678,987654321)
print(atharvatm.pincode)

print(atharvatm.language())    





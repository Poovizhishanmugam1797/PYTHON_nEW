ID=int(input("Employee Id  : "))
Basicpay=int(input("Basic Salary : "))
Allowances=int(input("Allowances   : "))
gross=Basicpay+Allowances
if(gross>10000):
     income=(20/100)*gross
net=gross-income
print(" Net   Salary : ",net)
print(" Gross Salary : ",gross)
print(" Basic Pay    : ",Basicpay)
print(" Id           : ",ID)
print(" Allowances   : ",Allowances)
print(" Income       : ",income)

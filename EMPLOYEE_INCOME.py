ID=int(input("Employee Id  : "))
Basicpay=int(input("Basic Salary : "))
Allowances=int(input("Allowances   : "))
gross=Basicpay+Allowances
if(gross>=100001 and gross<=20000):
     income=(20/100)*gross
     print(" INCOME : ",income)
elif(gross<5000):
     print(NIL)
     print(" INCOME : ",income)
elif(gross>=5001 and gross<=10000):
     income=(10/100)*gross
     print(" INCOME : ",income)
elif(gross>20000):
     income=(30/100)*gross
     print(" INCOME : ",income)

     
     


     

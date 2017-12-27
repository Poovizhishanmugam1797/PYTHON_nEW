n1=input("Enter the String : ")
s1=n1.replace(" ","")
lt1=[]
lt=[]
for i in range(0,len(s1),2):
     lt.append(s1[i])
     
s2="".join(lt)
print(s2)
s3=s2[::-1]
print(s3)
     
     
     

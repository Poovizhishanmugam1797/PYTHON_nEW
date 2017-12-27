def palindrome(n1):
     n2=n1[::-1]
     if(n2==n1):
          print("Palindrome ")
     else:
          print(" Not Palindrome ")
def vowel(n1):
     count=0
     for i in range(0,len(n1)):
          n2=n1[i].tolower()
          if(n2=='a' or n2=='e'or n2=='i'or n2=='o'or n2=='u'):
               count=count+1
     print(count)          
               
def punc(n1):
     i=0
     s1=['*','/','=','!','[]','()','-',':',';','"']
     lt=[]
     for i in range(0,len(n1)):
          if(n1[i] not in s1):
              l1=lt.append(n1[i])
     s="".join(lt)
     print(s)

def capital(n1):
     count=0
     for i in range(0,len(n1)):
          if(n1[i].isupper()):
               count=count+1
     print(count)
def joinreverse(n1):
     s2="".join(n1)
     

n1=input("Enter the String ")
ch=int(input("Enter ur choice "))
if(ch==1):
     capital(n1)
    
if(ch==2):
     palindrome(n1)
if(ch==3):
     vowel(n1)
if(ch==4):
     punc(n1)
 
     
     
          
     
          
          
          
          

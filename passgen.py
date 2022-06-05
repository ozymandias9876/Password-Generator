from random import *
import string
print(" 1.Numeric \n 2.AlphaNumeric \n 3.Alphanumeric with Ascii")
x=int(input("Select the type of password:"))
y=int(input("Enter Password Length: "))
alphabet=list(string.ascii_letters)
digit=list(string.digits)
ascii_c=list(string.ascii_letters + string.digits + "!@#$%^&*()")
password=[]
if(x==1):
	for i in range(y):
		password.append(choice(digit))
elif(x==2):
	for i in range(y):
		password.append(choice(alphabet+digit))
else:
	for i in range(y):
		password.append(choice(ascii_c))
z="".join(password)
print(z)

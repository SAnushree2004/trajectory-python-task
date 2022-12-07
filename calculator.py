a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Floor division\n7.Remainder")
x=int(input("Enter choice:"))
if(x==1):
	print(a+b)
elif(x==2):
	print(a-b)
elif(x==3):
	print(a*b)
elif(x==4):
	print(a/b)
elif(x==5):
	print(a**b)
elif(x==6):
	print(a//b)
elif(x==7):
	print(a%b)
else:
	print("Wrong Choice!!")

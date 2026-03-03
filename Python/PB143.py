n1=int(input("Enter your first number:"))
n2=int(input("Enter your second number:"))
n3=int(input("Enter your third number:"))

if n1==n2 and n2==n3 and n3==n1:
    result=(n1+n2+n3)*3
else:
    result=(n1+n2+n3)
print(result)
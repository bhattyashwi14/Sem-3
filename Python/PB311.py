str=input("Enter your string:")
upp=0
low=0
dig=0
for i in range(len(str)):
    if str[i].isupper():
        upp+=1
    elif str[i].islower():
        low+=1
    elif str[i].isdigit():
        dig+=1
print("Uppercase letters:",upp)
print("Lowercase letters:",low)
print("Digits:",dig)
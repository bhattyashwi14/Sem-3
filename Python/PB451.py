L=eval(input("Enter your list:"))
summ=0
for i in range(len(L)):
    if L[i]==13:
        continue
    elif L[i-1]==13 and i!=0:
        continue
    else:
        summ+=L[i]
print("Sum without unlucky number:",summ)
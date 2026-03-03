L=eval(input("Enter your list:"))
s=int(input("Enter shift:"))
l=[]
if s>len(L):
    print("Shift shall not be greater than length of list")
else:
    for i in range(s,len(L)):
        l.append(L[i])
    for i in range(s):
        l.append(L[i])
    print(l)
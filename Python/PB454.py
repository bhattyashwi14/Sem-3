L=input("Enter string:")
l=[')','}',']']
l1=[]
if L[0] in l:
    print("Unbalanced string")
else:
    for i in range(len(L)):
        if L[i]=='}' and l1[-1]=='{':
            l1.pop()
        elif L[i]==')' and l1[-1]=='(':
            l1.pop()
        elif L[i]==']' and l1[-1]=='[':
            l1.pop()
        else:
            l1.append(L[i])
    if len(l1)==0:
        print("String is balanced")
    else:
        print("String is unbalanced")

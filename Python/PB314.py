strr=input("Enter the string:")
key=int(input("Enter the key:"))
upp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
en=""
for i in range(len(strr)):
    if strr[i].isupper():
        j=((upp.index(strr[i]))+key)%26
        en=en+upp[j]
    elif strr[i].islower():
        j=((low.index(strr[i]))+key)%26
        en=en+low[j]
    elif strr[i].isdigit():
        j=str((int(strr[i])+key)%10)
        en=en+j
    elif strr[i]==" ":
        en=en+" "
print("Encrypted msg:",en)
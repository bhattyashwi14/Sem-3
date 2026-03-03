print("Enter 1 if you want to encrypt a message")
print("Enter 2 if you want to decrypt a message")
n=int(input("Enter your choice:"))

if n==1:
    msg=input("Enter your message:")
    key=int(input("Enter your key:"))
    en=""
    for i in range(key):
        en+=msg[i::key]
    print("Encrypted messaged:",en)
elif n==2:
    msg1=input("Enter your message:")
    key1=int(input("Enter your key:"))
    den=""
    l=[]
    start=0
    part=len(msg1)//key1
    extra=len(msg1)%key1
    #extra are the number of groups whose length will be part+1
    #and key-extra is the group with length=part
    for i in range(key1):
        if i<extra:
            l.append(msg1[start:start+part+1])
            start=start+part+1
        else:
            l.append(msg1[start:start+part])
            start=start+part
    for i in range(0,part if extra==0 else part+1):
        for j in l:
            if len(den)==len(msg1):
                break
            den=den+j[i]
    print("Decrypted message:",den)
    print()
    s=den.lower()
    d={}
    ss=s.split(" ")
    for i in range(len(ss)):
        L=[]
        for j in range(len(ss)):
            if ss[i][0]==ss[j][0]:
                L.append(ss[j])
                d[ss[i][0]]=L
    print(d)





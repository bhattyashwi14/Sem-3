passcode=input("Enter your passcode:")
upp=0
space=0
dig=0
speacial=['$','@','_']
sp=0
for i in range(len(passcode)):
    if passcode[i].isupper():
        upp+=1
    elif passcode[i].isdigit():
        dig+=1
    elif passcode[i]==" ":
        space+=1
    elif passcode[i] in speacial:
        sp+=1
if upp>0 and dig>0 and sp>0 and space==0 and len(passcode)>=8:
    print("Valid passcode")
else:
    print("Invalid passcode")
    if len(passcode)<8:
        print("Passcode be atleast 8 character long")
    if dig==0:
        print("Passcode should have atleast 1 digit")
    if upp==0:
        print("Passcode should have atleast 1 uppercase alphabet")
    if sp==0:
        print("Passcode should have atleast 1 special character")
    if space>0:
        print("Passcode should not have space")

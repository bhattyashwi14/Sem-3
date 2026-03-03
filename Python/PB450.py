d={"student0":'Student@0',"student1":'Student@11',"student2":'Student@121',
"student3":'Student@052',"student4":'Student@01278',"student5":'Student@0125', "Student6":'Student@042',
"student7":'Student@07800',"student8":'Student@012'}
count=1

def update_pass(user):
    upd=input("Enter updated passcode:")
    upp=0
    low=0
    sp=0
    spp=['@','_','$']
    space=0
    dig=0
    for i in range(len(upd)):
        if upd[i].isupper():
            upp+=1
        elif upd[i].islower():
            low+=1
        elif upd[i] in spp:
            sp+=1
        elif upd[i]==" ":
            space+=1
    if len(upd)>=8 and len(upd)<=15 and upp>0 and low>0 and sp>0 and space==0:
        d[user]=upd
        return True
    else:
        return False
    
while count<=3:
    user=input("Enter user name:")
    paas=input("Enter passcode:")
    if user in d:
        if d[user]==paas:
            c=1
            while(c<=3):
                ans=update_pass(user)
                if ans:
                    d=dict(sorted(d.items(),key=lambda x: len(x[1])))
                    print(d)
                    break
                else:
                    print("Follow the passcode format")
                c+=1
            if c>3:
                print("Try updating passcode after 24 hours")
            break
        else:
            print("Enter valid passcode")
    else:
        print("Enter valid username")
    count+=1
if count>3:
    print("Try after 24 hours")

for n in range(1,101,1):
    temp=n 
    temp1=n
    count=0
    rev,sum1,summ=0,0,0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    while rev>0:
        count+=1
        r=rev%10
        sum1=sum1+r**count
        rev=rev//10
    #if sum1==temp1:
        #print(temp1,"is Disarium")
    #else:
        #print(temp1,"is Not Disarium")
    while temp>0:
        r=temp%10
        summ=summ+r
        temp=temp//10
    #if temp1%summ==0:
        #print(temp1,"is Harshad Number")
    #else:
        #print(temp1,"is Not Harshad Number") 
    if temp1==summ and temp1==sum1:
        print(temp1,"is both Disarium and Harshad number")


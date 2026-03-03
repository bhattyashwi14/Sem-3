start=int(input("Enter start of range:"))
end=int(input("Enter end of range:"))
for i in range(start,end+1,1):
    n=i
    while n!=1 and n!=4:
        summ=0
        while n>0:
            r=n%10
            summ=summ+r**2
            n=n//10
        n=summ
    if n==1:
        print(i,"is a Happy Number")
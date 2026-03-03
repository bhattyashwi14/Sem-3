n=int(input("Enter value of n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==j:
            print(1,end=" ")
        else:
            print(0,end=" ")
    for j in range(i,n):
        print(0,end=" ")
    print()
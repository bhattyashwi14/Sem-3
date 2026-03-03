n=int(input("Enter value for n:"))
k=0
for i in range(1,n+1):
    k=k+i
    l=k
    for j in range(1,i+1):
        print(l,end=" ")
        l-=1
    print()
L=eval(input("Enter your list:"))
for i in range(len(L)):
    even=0
    odd=0
    x=L[i]
    L.pop(i)
    # print(L,"after removing",x)
    for j in range(len(L)):
        if j%2==0:
            even+=L[j]
        if j%2!=0:
            odd+=L[j]
    if even==odd:
        print("Special element is:",x,"at index",i)
        print("Equal sums at odd and even places:",L)
    L.insert(i,x)
    
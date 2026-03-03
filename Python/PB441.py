L=eval(input("Enter your list:"))
S=set(L)
summ=0
product=1
for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            if i!=j and j!=k and k!=i:
                print(L[i],L[j],L[k])
for i in S:
    summ+=i
    product*=i
print("No. of unique elements:",len(S))
print("Sum excluding duplicates:",summ)
print("Product excluding duplicates:",product)


        

L=eval(input("Enter your list:"))
for i in range(3):
    for j in range(3):
        if j>i:
            L[i][j],L[j][i]=L[j][i],L[i][j]
    for i in L:
        i.reverse()
print(L)
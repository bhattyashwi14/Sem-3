L=eval(input("Enter your list:"))
L.sort()
Length=0
ans=""
if L[0]<L[-1]:
    Length=len(L[0])
else:
    Length=len(L[-1])
for i in range(Length):
    if L[0][i]==L[-1][i]:
        ans+=L[0][i]
    else:
        break
if ans=="":
    ans=-1
print("Prefix:",ans)
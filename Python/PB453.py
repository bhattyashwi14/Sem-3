L=eval(input("Enter your list:"))
for i in range(0,len(L),2):
   L.insert(i+1,L.pop())
print(L)

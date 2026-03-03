n=int(input("Enter your number:"))
product=1
count=0
while n>0:
    r=n%10
    if r%2!=0:
        product=product*r
        count+=1
    n=n//10
if count==0:
    product=0
print("Product of odd numbers=",product)

n=input("Enter your number:")
s=int(input("Enter the shift:"))
def shift(n,s):
    change=""
    if s>len(n):
        change=n[::-1]
    else:
        for i in range(s,len(n)):
            change+=n[i]
        for i in range(0,s):
            change+=n[i]
    return change
print(shift(n,s))
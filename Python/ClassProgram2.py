units=int(input("Enter your electricity units used:"))
cost=0
if units<0:
    print("Please enter valid no. of units")
elif units<=150:
    cost=150*3
elif units<=300 and units>150:
    cost=(150*3)+100+(3.75*(units-150))
elif units<=450 and units>300:
    cost=(150*3)+(100+3.75*(150))+(250+(units-300)*400)
elif units<=600 and units>450:
    cost=(150*3)+(100+3.75*(150))+(250+(300)*400)+(300+(units-450)*4.25)
elif units>600:
    cost=(150*3)+(100+3.75*(150))+(250+(300)*400)+(300+(450)*4.25)+(400+(units-600)*5)
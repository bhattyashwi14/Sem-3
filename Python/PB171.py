grade=input("Enter grade level:")
tier=int(input("Enter the tier of the city:"))
ta=900
pt=200
if grade=="A":
    bp=60000
    oa=8000
    dra=0.5*bp
elif grade=="B":
    bp=50000
    oa=7000
elif grade=="C":
    bp=40000
    oa=6000
elif grade=="D":
    bp=30000
    oa=5000
elif grade=="E":
    bp=20000
    oa=4000
elif grade=="F":
    bp=10000
    oa=3000

if tier==1:
    hra=0.3*bp
elif tier==2:
    hra=0.2*bp
elif tier==3:
    hra=0.1*bp

dra=0.5*bp
pf=0.11*bp

gross_pay=bp+hra+dra+oa+ta-pt-pf
annual_income=gross_pay*12

if annual_income<=250000:
    tax=0
elif annual_income<=500000 and annual_income>250000:
    tax=(annual_income-250000)*0.05
elif annual_income<=750000 and annual_income>500000:
    tax=12500+(annual_income-500000)*0.1 
elif annual_income>750000 and annual_income<=1000000:
    tax=37500+(annual_income-750000)*0.15
elif annual_income<=1250000 and annual_income>1000000:
    tax=75000+(annual_income-1000000)*0.2
elif annual_income>1250000 and annual_income<=1500000:
    tax=125000+(annual_income-1250000)*0.25
elif annual_income>1500000:
    tax=187500+(annual_income-1500000)*0.3

print("Gross Pay=",gross_pay)
print("Annual income=",annual_income)
print("Income Tax=",tax)







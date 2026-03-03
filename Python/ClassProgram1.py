class10=int(input("Enter your marks obtained in 10th:"))
class8=int(input("Enter your marks of class 8:"))
grad=int(input("Enter marks obtained in graduation:"))
stream=input("Enter your stream chosen for graduation:")
pg_stream=input("Enter your stream for post graduation:")
if class10>80 and class8>80:
    if stream!=pg_stream:
        grad=grad-5
    if grad>70:
        print("Congratulation, you are elligible for the PG program")
    else:
        print("Sorry, you're not elligible for this PG program")
else:
    print("Sorry, you're not elligible for this PG program")
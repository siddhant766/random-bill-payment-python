print("what is the total bill ?")
a=float(input("total bill : "))
b=float(input("what amount of  tip you will like to pay: "))
c=a*b/100
d=int(input("how many people will split this bill: "))
e= (a+c)/d

print(f"each person should pay{round(e,2)}")

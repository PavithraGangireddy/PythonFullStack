base=5000
price=base
seats= int(input("enter the no of seats type:"))
days=int(input("enter no of booking days:"))
festival =(input("enter festival or not:")).lower == "true"
age= int(input("enter your age:"))
if seats == "buisness":
    price *=1.4
elif seats =="permiun":
    price *=1.2

if days >30:
    price*=0.9
elif days<7:
    price*=1.25
if festival:
    price*=1.2
if age>60:
    price*=0.05
print(price)

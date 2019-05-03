name=input("enter your name :")
unit=input("(L)bs or (K)gs=")
weight=int(input("Enter your weight="))
if unit.upper() =="L":
    convert=weight*0.45
    print(f'{name} weighs {convert} kgs')
else:
    convert=weight//0.45
    print(f"{name} weighs {convert} pounds")


print("1 - lngth \n2 - temprature ")
choise = int(input("enter your choice : "))

#code for length
 
if choise == 1:
    length = int(input("enter your length :") )
    print("1 -kilometer \n2 - feet ")
    # user choise
    length_choise = int(input("enter your choise :"))

    if length_choise == 1:
        print(f"{length/1000} kilometer")
    elif length_choise == 2:
        print(f"{length * 3.28084}feet")

#code for tem.

elif choise == 2:
    tem = float(input("enter your temperature in celcius : "))
    print(f"{(tem * 9/5)+32} fehrenheit")

else:
    print("INVALID CHOISE")


## calculator
number1 = float(input("Enter first number :"))
number2 = float(input("Enter second number :"))
operation = input("enter operator +,-,*,/,%  ")
if operation=="+":
    print(number1+number2)
elif operation=="-":
    print(number1-number2)
elif operation=="*":
    print(number1*number2)
elif operation=="/":
    if number2==0:
        print("infinity")
    else:
        print(number1/number2)  
elif operation=="%":
    print(number1%number2)
else:
    print("invalid operator")          

a = int(input("enter the one side of triangle"))
b = int(input("enter the second side of the triangle"))
c = int(input("enter the third side of the triangle"))
if((a==b and b==c)):
    print("triangle is equilateral")
elif((a==b and b!=c) or (a==c and b!=a)):
    print("triangle is isoscale")
elif((a!=b and b!=c) or (a!=c and b!=a)):
    print("triangle is scalar")        
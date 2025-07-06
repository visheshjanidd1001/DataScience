#Grading Calculator
print("Please Enter Your Marks out of Hundred !")
p = int(input("Enter phyics marks : "))
c = int(input("Enter chemistry marks : "))
m = int(input("Enter maths marks : "))

sum = p+c+m

per = sum/300 * 100

print("Your Percentage is : " , per)
if(per>=90):
    print("your grade is A ")
elif(per>=80):
    print("your grade is B ")
elif(per>=70):
    print("your grade is C ")
else :
    print("You Are Failed !! ")

    

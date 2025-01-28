a = float(input("Enter side a : "))
b = float(input("Enter side b : "))
c = float(input("Enter side c : "))

if(a==b and b==c):
    print("It is an equilateral triangle.")
elif(a==b or a==c):
    print("It is an isosceles triangle.")
else:
    print("It is a scalene triangle.")
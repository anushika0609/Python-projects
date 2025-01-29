num = input("Enter the number : ")
if(num.startswith("-")):
    print("Number is negative.")
elif(num.startswith("0")):
    print("Number is zero.")
else:
    print("Number is positive.")
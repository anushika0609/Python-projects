num = int(input("Enter the number of month : "))

if(5>=num>=3):
    print("Spring season")
elif(8>=num>=6):
    print("Summer season")
elif(11>=num>=9):
    print("Autumn season")
elif(num==12 or num==1 or num==2):
    print("Winter season")
else:
    print("Please enter a valid month.")
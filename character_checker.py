character = input("Enter the character : ")
if (character.isalpha()):
    print("Given character includes alphabets.")
elif(character.isalnum()):
    print("Given character includes alphabets and numbers.")
else:
    print("Given character includes special characters.")
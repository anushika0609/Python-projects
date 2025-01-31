str1 = str(input("Enter the string : "))
str2 = str(input("Enter substring : "))
if(str2 in str1):
    print("Given substring exists. Index of substring is", str1.index(str2))
else:
    print("Given substring does not exist.")
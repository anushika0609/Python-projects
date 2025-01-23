#If a string starts with a vowel
string = str(input("Write the string : "))
if(string.startswith("a") or string.startswith("A") or string.startswith("i")
     or string.startswith("E") or string.startswith("e") or string.startswith("I")
     or string.startswith("o") or string.startswith("u") or string.startswith("U")):
    print("Given string starts with a vowel")

else:
    print("Given string starts with a consonant")    
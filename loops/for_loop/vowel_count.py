vowels = "a, e, i, o, u"
word = "education"
count = 0
for char in word:
    if char in vowels:
        count+=1
print("Total number of vowels are", count) 
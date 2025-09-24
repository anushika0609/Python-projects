n = int(input("Enter the number of elements : "))
tup = ()
temp = list(tup)
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    temp.append(ele)
tup = tuple(temp)
print("Given tuple is : ",tup)

num = int(input("Enter the value for checking : "))
exists = False
for value in tup:
    if(value == num):
        exists = True

if(exists == True):
    print(f"{num} exists in the tuple")
else:
    print(f"{num} doesn't exist in the tuple")
n = int(input("Enter number of elements : "))
list = []
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    list.append(ele)
print(list)

num = int(input("Enter number : "))
present = False
for value in list:
    if(value == num):
        present = True
if(present == True):
    print(f"{num} exists in list")
else:
    print(f"{num} doesn't exit in list")
        
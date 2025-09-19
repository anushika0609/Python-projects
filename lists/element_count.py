n = int(input("Enter number of elements : "))
list = []
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    list.append(ele)
print(list)

num = int(input("Enter number for count : "))
count = 0
for value in list:
    if(num == value):
        count = count + 1
    else:
        print("Number not found")
        
print(f"Count of {num} is : ", count)

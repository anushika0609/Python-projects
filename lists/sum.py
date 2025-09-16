n = int(input("Enter the number of elements : "))
list = []
for i in range(n):
    element = input(f"Enter element {i+1} : ")
    list.append(element)
print(list)

sum = 0
for i in list:
    value = int(i)
    sum = sum + value
print(f"Sum of elements in the list is : {sum}")

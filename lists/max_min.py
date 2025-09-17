n = int(input("Enter the number of elements : "))
list = []
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    list.append(ele)
print(list)

small = float('inf')
large = float('-inf')

for value in list:
    if(value>large):
        large = value
    elif(value<small):
        small = value
        
print("smallest no. : ",small,"and largest no. : ",large)
        
        
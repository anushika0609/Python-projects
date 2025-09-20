n = 5
tup = ( )
list = list(tup)
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    list.append(ele)
tup = tuple(list)
print(tup)

print("Element at first position : ",tup[0]," and element at last position : ",tup[n-1])
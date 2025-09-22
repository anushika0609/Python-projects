a=0
b=1
print(a,b, end=" ")
for i in range(8):
    num = a+b
    print(num, end=" ")
    a,b=b,num
    
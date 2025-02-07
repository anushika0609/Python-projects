num=int(input("Enter the number : "))
sum=0
i=1
while i<=num :
    last_digit=i%10
    sum+=last_digit
    i+=1
    print("Sum : ",sum)
    
    
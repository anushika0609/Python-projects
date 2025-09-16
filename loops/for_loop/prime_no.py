num = int(input("Enter the number : "))
is_prime = True

for i in range(2, int(25**0.5+1)):
    if num%i==0:
        is_prime=False
        break
    
if is_prime and num > 1 :
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
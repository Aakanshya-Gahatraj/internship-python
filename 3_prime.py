def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n= int(input("Enter a number: "))

if isPrime(n)==True:
    print("Your number is prime.")
else:
    print("Your number is not prime.")
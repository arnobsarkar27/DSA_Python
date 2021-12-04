# Check whether a number is prime or not.

def is_prime(num):
    factors = []
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    
    if factors == [1,num]:
        return True
    else:
        return False

def check(num):
    if num==1:
        print("{} is a composite number.".format(num))
    else:
        if is_prime(num):
            print("{} is prime.".format(num))
        else:
            print("{} is not prime.".format(num))


num = int(input("Enter the number: "))
check(num)

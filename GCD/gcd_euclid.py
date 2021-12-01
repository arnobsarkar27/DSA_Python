# Euclid's algorithm for GCD
# Still under construction

def gcd(num1,num2):
    # Here, num1 < num2 is assumed by default.
    if num1 > num2:
        (num1,num2) = (num2,num1)

    diff = num2 - num1
    starting_point = num1
    # Assume the difference is smaller than num1. Else, just swap it like we did earlier for num1 and num2.
    if diff > num1:
        (starting_point,diff) = (diff,starting_point)
    print(starting_point)
    print(diff)
    for i in range(starting_point,diff-1,-1):
        if diff%i==0 and num1%i==0: # incorrect at this point
            return(i)

num1 = int(input("Enter First number: "))
num2 = int(input("Enter second number: "))
print("Highest common Factor: ",gcd(num1,num2))

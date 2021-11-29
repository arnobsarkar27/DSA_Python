# No use of list
# This uses minimum of the three numbers.

def gcd(num1,num2):
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            greatest_common_factor = i

    return(greatest_common_factor)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Hightst common factor: ",gcd(num1,num2))
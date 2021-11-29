#A much shorter program algorithm for GCD of three numbers
# This uses minimum of the three numbers.

def gcd(num1,num2,num3):
    common_factors = []
    common_factors = [i for i in range(1,min(num1,num2,num3)+1) if num1%i==0 and num2%i==0 and num3%i==0]

    return(common_factors[-1])

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Highest common factor: ",gcd(num1,num2,num3))

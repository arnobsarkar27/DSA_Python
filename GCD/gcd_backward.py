# Backward GCD
# No use of list here.
# Immediately break the loop when we get the highest common factor

def gcd_backwards(num1,num2):
    for i in range(min(num1,num2),0,-1):
        if num1%i==0 and num2%i==0:
            hcf = i
            break
    return(hcf)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Highest Common Factor: {}".format(gcd_backwards(num1,num2)))

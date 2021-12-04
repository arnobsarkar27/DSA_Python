# Euclid's algorithm for GCD
# Will try to make it shorter

#Assume n > m
def gcd_euclid(n,m):
    if n%m==0:
        return(m)
    diff = n - m
    return(gcd_euclid(max(diff,m),min(diff,m)))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if(num1 < num2):
    (num1,num2) = (num2,num1)
diff = num1 - num2
print("Highest Common Factor: ", gcd_euclid(max(diff,num2),min(diff,num2)))

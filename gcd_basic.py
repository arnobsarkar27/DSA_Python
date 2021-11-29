#Learning DSA using Python
#Basic Greatest Common Divisor Algorithm

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

num1_factors = []
num2_factors = []
common_factors = []

num1_factors = [i for i in range(1,num1+1) if num1%i==0]
num2_factors = [i for i in range(1,num2+1) if num2%i==0]

print("Factors:")
print("{}: {}".format(num1,num1_factors))
print("{}: {}".format(num2,num2_factors))

for i in range(len(num1_factors)):
    for j in range(len(num2_factors)):
        if num1_factors[i] == num2_factors[j]:
            common_factors.append(num1_factors[i])
            break

print("List of common factors: ", common_factors)
print("Highest Common Factor: ",common_factors[-1])

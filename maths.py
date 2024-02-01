# Ask the user to input 2 values and store them in variables num1 num2
num1, num2 = input('Enter two numbers: ').split()
# Convert the string into regular number integer
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Substract values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the value and store in quotient
quotient = num1 / num2

# Use modulus on the value to find the remainder
remainder = num1 % num2

# Print the result
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
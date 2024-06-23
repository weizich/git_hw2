# Input polynomial string and value of x
poly_string = input("Enter the polynomial string: ")
x_value = float(input("Enter the value of X: "))

# Split the polynomial string into terms
terms = poly_string.split('+')

# Initialize the result
result = 0

# Initialize exponent and coefficient
exponent = 0
coefficient = 0

# Initialize index
index = 0

# Repeat until all terms are evaluated
while index < len(terms):
    # Split each term into coefficient and exponent parts
    parts = terms[index].split('X^')
    if len(parts) == 1:
        coefficient = int(parts[0])
        exponent = 0
    else:
        coefficient = int(parts[0])
        exponent = int(parts[1])

    # Evaluate the term and add to the result
    result += coefficient * (x_value ** exponent)

    # Move to the next term
    index += 1

# Print the result
print("Result of evaluating the polynomial:", result)

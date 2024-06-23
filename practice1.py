sequence = input("Enter a sequence of numbers separated by whitespace: ")
sequence = sequence.split(" ")
sequence = [int(i) for i in sequence]

LICS = [sequence[0]]  # Initialize LICS with the first element of the sequence

for x in sequence[1:]:
    if x > LICS[-1]:  # Compare x with the last element of LICS
        LICS.append(x)

print("The longest increasing subsequence is:", LICS)

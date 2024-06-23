time_input = input("Enter the time in 'h:m:s' format: ")

# Splitting the time string into hours, minutes, and seconds
h, m, s = time_input.split(':')

# Converting hours, minutes, and seconds to integers
h = int(h)
m = int(m)
s = int(s)

# Converting hours, minutes, and seconds to seconds
total_seconds = h * 3600 + m * 60 + s

print("Total seconds in a day:", total_seconds)
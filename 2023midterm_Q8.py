# Take input for theater dimensions
rows = int(input("Enter the number of rows in the theater: "))
cols = int(input("Enter the number of columns in the theater: "))

# Take input for reserved seats
reserved_seats_input = input("Enter reserved seats (format: 'row,col|row,col|...'): ")
reserved_seats = reserved_seats_input.split('|')

# Create seating arrangement
seating_arrangement = [['A'] * cols for _ in range(rows)]

# Mark reserved seats as 'R' in the seating arrangement
for seat in reserved_seats:
    seat_coords = seat.split(',')
    row = int(seat_coords[0])
    col = int(seat_coords[1])
    if 0 <= row < rows and 0 <= col < cols:
        seating_arrangement[row][col] = 'R'

# Display seating arrangement
for row in seating_arrangement:
    print(' '.join(row))

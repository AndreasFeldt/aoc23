from collections import defaultdict

# Read the input file
input_file = open('input.txt', 'r').read().strip()

lines = input_file.split('\n')

# Convert input into a 2D grid
grid = [[char for char in line] for line in lines]
num_rows = len(grid)
num_cols = len(grid[0])

p1_total = 0
gears_with_numbers = defaultdict(list)

# Iterate through the grid to find numbers and their adjacent gears
for row in range(num_rows):
    gears = set()  # Stores positions of '*' characters next to the current number
    number = 0
    has_component = False

    for col in range(num_cols + 1):
        if col < num_cols and grid[row][col].isdigit():
            number = number * 10 + int(grid[row][col])
            # Check adjacent positions for gears and components
            for r_offset in [-1, 0, 1]:
                for c_offset in [-1, 0, 1]:
                    if 0 <= row + r_offset < num_rows and 0 <= col + c_offset < num_cols:
                        ch = grid[row + r_offset][col + c_offset]
                        if not ch.isdigit() and ch != '.':
                            has_component = True
                        if ch == '*':
                            gears.add((row + r_offset, col + c_offset))
        elif number > 0:
            # Update gear positions with corresponding numbers
            for gear in gears:
                gears_with_numbers[gear].append(number)
            if has_component:
                p1_total += number
            number = 0
            has_component = False
            gears = set()

# Print the total from part 1
print(p1_total)

p2_total = 0
for key, value in gears_with_numbers.items():
    # Calculate the product of numbers associated with gears that have exactly 2 numbers
    if len(value) == 2:
        p2_total += value[0] * value[1]

# Print the total from part 2
print(p2_total)

def read_file_to_list(filepath: str) -> list:
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]

def calculate_previous_number(sequence: list) -> int:
    difference_sequences = []
    difference_sequences.append(sequence)
    while any(difference_sequences[-1]):
        current_difference = []
        for index in range(len(difference_sequences[-1]) - 1):
            difference = difference_sequences[-1][index + 1] - difference_sequences[-1][index]
            current_difference.append(difference)
        difference_sequences.append(current_difference)
    difference_sequences.reverse()
    previous_number = 0
    for level in difference_sequences:
        previous_number = level[0] - previous_number
    return previous_number

def process_file_and_calculate(filename: str):
    file_contents = read_file_to_list(filename)
    total = 0
    for line in file_contents:
        number_sequence = [int(num) for num in line.split()]
        total += calculate_previous_number(number_sequence)

    print(total)

def calculate_previous_number(sequence: list) -> int:
    difference_sequences = []
    difference_sequences.append(sequence)
    while any(difference_sequences[-1]):
        current_difference = []
        for index in range(len(difference_sequences[-1]) - 1):
            difference = difference_sequences[-1][index + 1] - difference_sequences[-1][index]
            current_difference.append(difference)
        difference_sequences.append(current_difference)
    difference_sequences.reverse()
    previous_number = 0
    for level in difference_sequences:
        previous_number = level[0] - previous_number
    return previous_number

def process_file_and_calculate(filename: str):
    file_contents = read_file_to_list(filename)
    total = 0
    for line in file_contents:
        number_sequence = [int(num) for num in line.split()]
        total += calculate_previous_number(number_sequence)

    print(total)

if __name__ == "__main__":
    input_file = "day9/input.txt"
    process_file_and_calculate(input_file)

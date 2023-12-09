def get_previous_number(numbers: list) -> int:
    step_list = [numbers]

    while any(step_list[-1]):
        this_step = [step_list[-1][i + 1] - step_list[-1][i] for i in range(len(step_list[-1]) - 1)]
        step_list.append(this_step)

    step_list.reverse()

    result = 0
    for step in step_list:
        result = step[0] - result

    return result

def file_to_list(filename: str) -> list:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    filename = "numbers.txt"
    content = file_to_list(filename)
    result = 0

    for numbers in content:
        numbers = [int(i) for i in numbers.split()]
        result += get_previous_number(numbers)

    print(result)

if __name__ == "__main__":
    main()
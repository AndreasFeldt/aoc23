def possible(game):
    is_possible = True
    max_values = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    for round in game:
        cubes = round.split(', ')
        for cube in cubes:
            color = cube.split(' ')[1]
            amount = int(cube.split(' ')[0])
            if amount > max_values[color]:
                is_possible = False
        
    return is_possible

def main():
    game_sum = 0

    with open('day2/puzzle1/input.txt') as data:
        lines = data.read().splitlines()


    for line in lines:
        game = line.split(': ')[1].split('; ')
        game_id = int(line.split(': ')[0].split(" ")[1])
        if possible(game):
            game_sum += game_id
    print(game_sum)
    
if __name__ == '__main__':
    main()
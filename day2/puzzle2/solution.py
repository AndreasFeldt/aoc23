import math

def possible(game):
    colors = {
        'red' : 0,
        'blue' : 0,
        'green' : 0
    }
    for round in game:
        cubes = round.split(', ')
        for cube in cubes:
            color = cube.split(' ')[1]
            amount = int(cube.split(' ')[0])
            if amount > colors[color]:
                colors[color] = amount
                
    power = math.prod(colors.values())
    return power


def main():
    game_sum = 0
    with open('day2/puzzle2/input.txt') as data:
        lines = data.read().splitlines()
    for line in lines:
        game_data = line.split(': ')[1].split('; ')
        game_sum += possible(game_data)

    print(game_sum)
    
if __name__ == '__main__':
    main()
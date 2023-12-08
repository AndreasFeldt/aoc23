from termcolor import colored
from itertools import cycle
from halo import Halo



# input_text = """
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# """.strip().splitlines()

input_text = open('day8/input.txt', 'r').read().strip().splitlines()

def find_path(instr: str, ways: dict, startpos: list):
    n = 0
    instr = cycle(instr)
    while True:
        
        bb = []
        for y in startpos:
            if y.endswith("Z"):
                bb.append(True)
            else:
                bb.append(False)

        if all(bb):
            break
        LR = next(instr)
        for x in startpos:
            start_index = startpos.index(x)
            b = x
            b = ways[b][LR]
            startpos[start_index] = b
        n+=1
        
    return n

def make_new_map(_map) -> dict:
    new = {}
    for x in _map:
        if x:
            a = x.split(' = ')
            b,c = a[1].replace("(", "").replace(")", "").split(', ')
            new[a[0]] = {'R': c, 'L': b}
    return new


def main() -> str:
    instr = input_text[0]
    _map = input_text
    input_text.pop(0)
    spinner = Halo(text='Reformatting data ', spinner='dots', color='cyan')
    spinner.start()
    _map = make_new_map(_map)
    
    _map = dict(sorted(_map.items()))
    spinner.succeed('Data reformatted!')
    spinner = Halo(text='Bruteforcing paths!', spinner='dots', color='cyan',)
    spinner.start()

    b = []
    for x in _map.keys():
        if x.endswith('A'):
            b.append(x)
    
    result = find_path(instr, _map, b)
    spinner.succeed("Paths bruteforced!")
    return result
    
if __name__ == "__main__":
    try:
        spinner = Halo(text='', spinner='dots', color='cyan')
        spinner.succeed(f"Number of steps to Z: {colored(str(main()), color='red')}")
    except KeyboardInterrupt:
        print(colored("* Goodbye! 🙅‍♂️"))
        exit(0)
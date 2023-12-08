from termcolor import colored
from itertools import cycle
from halo import Halo




input_text = open('day8/input.txt', 'r').read().strip().splitlines()

def find_path(instr: str, ways: dict):
    n = 0
    ways = dict(sorted(ways.items()))
    instr = cycle(instr)
    b = list(ways.keys())[0]
    while b != 'ZZZ':
        LR = next(instr)
        b = ways[b][LR]
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
    _map = make_new_map(_map)
    with Halo(text=colored("Processing paths", 'red'), spinner='dots') as spinner:
        data = find_path(instr, _map)
        spinner.succeed(text=colored('All paths processed!', 'green'))
        return data
    
if __name__ == "__main__":
    with Halo(text="Processing", spinner='dots') as aa:
        aa.succeed(colored(f"Number of steps to ZZZ: ", "cyan")+ f"{colored(str(main()), 'red')}")
from tqdm import tqdm
from termcolor import colored
from itertools import cycle
# input_text = """
# LLR
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# """.strip().splitlines()

# input_text = """
# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# """.strip().splitlines()

input_text = open('day8/input.txt', 'r').read().strip().splitlines()

def find_path(instr: str, ways: dict):
    n = 0
    ways = dict(sorted(ways.items()))
    instr = cycle(instr)
    b = list(ways.keys())[0]
    print(b)
    while b != 'ZZZ':
        LR = next(instr)
        b = ways[b][LR]
        n+=1
        print(n)
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
    print(colored("* Processing", 'red'))
    return find_path(instr, _map)
    
if __name__ == "__main__":
    print(colored(f"* Number of steps to ZZZ: {str(main())}", "light_green"))
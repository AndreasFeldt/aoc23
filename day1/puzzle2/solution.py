from termcolor import colored

with open('input.txt', 'r') as f:
    lines = f.read()
mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
ret = 0
for string in lines.strip().split('\n'):
    first = None
    last = None
    aa = ""
    for a in string:
        digit = None
        if a.isdigit():
            digit = a
        else:
            aa += a
            for k,v in mapping.items():
                if aa.endswith(k):
                    digit = str(v)
        if digit is not None:
            last = digit
            if first is None:
                first = digit
    ret += int(first+last)

print("\n"+f"{colored('#', 'blue')}"*50+f"\n\n{colored('RESULT: ', 'green')}{colored(ret, 'green')}\n\n"+f"{colored('#', 'blue')}"*50)

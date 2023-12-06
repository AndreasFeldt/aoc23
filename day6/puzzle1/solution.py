input_text = """
Time:        35     93     73     66
Distance:   212   2060   1201   1044
""".strip().splitlines()


time = input_text[0].split(":")[1].split(' ')
time = [x for x in time if x]

distance = input_text[1].split(":")[1].split(' ')
distance = [x for x in distance if x]

max_combinations = []

for _time, _record in zip(time, distance):
    n = 0
    tmp = []
    while n <= int(_time):
        result = n * (int(_time) - n)
        if result > int(_record):
            tmp.append(result)
        n += 1
    max_combinations.append(tmp)

val = 0
for x in max_combinations:
    n = len(x)
    if val == 0:
        val = n
    else:
        val*=n
print(val)
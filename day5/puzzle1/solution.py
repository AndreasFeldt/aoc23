import re

def calc(values, mode):
    seeds = list(map(int, values[0].split(": ")[1].split(" ")))
    all_maps = {}
    for row in values[2:] + [""]:
        m = re.search("([a-z]+)-to-([a-z]+) map:", row)
        if m is not None:
            source_type, dest_type = m.group(1), m.group(2)
            maps = []
        m = re.search("([0-9]+) ([0-9]+) ([0-9]+)", row)
        if m is not None:
            dest, source, count = int(m.group(1)), int(m.group(2)), int(m.group(3))
            maps.append((dest - source, source, source + count - 1))
        if len(row) == 0:
            all_maps[source_type] = {
                "target": dest_type,
                "maps": maps,
            }

    ret = None

    if mode == 1:
        seeds = [(x, x) for x in seeds]
    else:
        seeds = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

    pos = "seed"
    while pos in all_maps:
        next_seeds = []
        temp = all_maps[pos]
        pos = temp["target"]
        while len(seeds) > 0:
            a, b = seeds.pop(0)
            found = False
            for offset, c, d in temp["maps"]:
                if c <= a <= d and c <= b <= d:
                    next_seeds.append((a + offset, b + offset))
                    found = True
                    break
                elif c <= a <= d:
                    next_seeds.append((a + offset, d + offset))
                    seeds.append((d + 1, b))
                    found = True
                    break
                elif c <= b <= d:
                    seeds.append((a, c - 1))
                    next_seeds.append((c + offset, b + offset))
                    found = True
                    break
                elif a < c and b > d:
                    seeds.append((d + 1, b))
                    seeds.append((a, c - 1))
                    next_seeds.append((c + offset, d + offset))
                    found = True
                    break
            if not found:
                next_seeds.append((a, b))
        seeds = next_seeds

    ret = min(x[0] for x in seeds)
    return ret

with open("input.txt") as f: 
    values = [x.strip("\r\n") for x in f.readlines()]

print("Part 1:", calc(values, 1))
print("Part 2:", calc(values, 2))
with open('input.txt', 'r') as f:
    input_text = f.read().splitlines()

dct = {i:1 for i in range(1, len(input_text) + 1)}
print(dct)

for i, row in enumerate(input_text, start=1):
    winning_nums = row.split("|")[0].split(" ")[2:]
    winning_nums = list(filter(lambda x: x != '', winning_nums))
    elf_nums = row.split("|")[1]

    n = 0
    for card in elf_nums.split():
        if card in winning_nums:
            n += 1
    
    for y in range(i + 1, i + n + 1):
        dct[y] = dct.get(y,0) + dct[i]

print(sum(dct.values()))
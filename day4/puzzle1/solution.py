with open('input.txt', 'r') as f:
    input_text = f.read()

total= 0
for card in input_text.splitlines():
    a = card.split(': ')
    card_n = a[0]
    card_numbers = a[1]
    
    b = card_numbers.split(' | ')
    elf_nums = b[0].split(" ")
    winning_nums = b[1].split(" ")
    winning_nums = list(filter(lambda x: x != '', winning_nums))
    
    card_points = 0
    first = True
    for num in elf_nums:
        for win_num in winning_nums:
            if num == win_num and not first:
                card_points = card_points * 2
            if num == win_num and first:
                card_points += 1
                first = False
    total += card_points
    print(card_n, elf_nums, winning_nums, card_points)


    print("Total points: ", total)
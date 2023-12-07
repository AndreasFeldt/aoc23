from statistics import mode
from tqdm import tqdm
from termcolor import colored

def create_card_rank_dict():
    card_values = "AKQJT98765432"
    reversed_values = card_values[::-1]
    value_dict = {rank: index for index, rank in enumerate(reversed_values)}
    return value_dict

def parse_input(input_data):
    return input_data.splitlines()

def get_card_value_and_rank(card, value_dict):
    rank, value = card.split()
    value = int(value)
    card_ranks = []
    
    if rank == rank[0] * 5:
        card_ranks.append(10)
        for _ in range(5):
            card_ranks.append(value_dict[rank[0]])
    elif rank.count(mode(list(rank))) == 4:
        card_ranks.append(9)
        for i in rank:
            card_ranks.append(value_dict[i])
    elif len(set(rank)) == 2:
        card_ranks.append(8)
        for i in rank:
            card_ranks.append(value_dict[i])
    elif rank.count(mode(list(rank))) == 3:
        card_ranks.append(7)
        for i in rank:
            card_ranks.append(value_dict[i])
    elif len(set(rank)) == 3 and rank.count(mode(list(rank))) == 2:
        card_ranks.append(6)
        for i in rank:
            card_ranks.append(value_dict[i])
    elif len(set(rank)) == 4 and rank.count(mode(list(rank))) == 2:
        card_ranks.append(5)
        for i in rank:
            card_ranks.append(value_dict[i])
    elif len(set(rank)) == 5:
        card_ranks.append(4)
        for i in rank:
            card_ranks.append(value_dict[i])
    return tuple(card_ranks), value

def calculate_total_score(cards, card_values):
    card_ranks = []
    
    for card in tqdm(cards, desc="Calculating Scores", unit="card"):
        rank, value = get_card_value_and_rank(card, card_values)
        card_ranks.append(rank)
    
    card_ranks = sorted(card_ranks)
    total_score = 0
    
    for index, rank in tqdm(enumerate(card_ranks), desc="Scoring", unit="rank", total=len(card_ranks)):
        for card in cards:
            a, b = get_card_value_and_rank(card, card_values)
            if a == rank:
                total_score += (index + 1) * b
                break
    
    return total_score

if __name__ == "__main__":
    card_values_dict = create_card_rank_dict()
    input_data = open('day7/input.txt', 'r').read()
    
    parsed_input = parse_input(input_data)
    total_score = calculate_total_score(parsed_input, card_values_dict)
    print(colored("Total score: " + str(total_score), 'light_green'))

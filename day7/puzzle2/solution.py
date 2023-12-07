from termcolor import colored
from tqdm import tqdm

CARD_VALUES = "J23456789TQKA"

def evaluate_hand_score(hand):
    best_score = calculate_best_hand_score(hand)
    additional_values = [get_card_value(card) for card in hand]
    return best_score + additional_values

def count_card_occurrences(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)

def calculate_best_hand_score(hand):
    cards = "23456789TQKA"
    if 'J' in hand:
        return max([calculate_best_hand_score(hand.replace('J', card, 1)) for card in cards])
    return count_card_occurrences(hand)

def get_card_value(card):
    return CARD_VALUES.index(card)

def main():
    input_data = open('day7/input.txt', 'r').read().strip().splitlines()
    scored_hands = []
    for line in tqdm(input_data, desc="Processing Hands", unit="hand"):
        hand, bid = line.split()
        scored_hands.append((evaluate_hand_score(hand), hand, int(bid)))
    
    scored_hands.sort()
    multiplier = 1
    total_score = 0
    
    for group in tqdm(scored_hands, desc="Calculating Total Score", unit="group"):
        bid = group[2]
        total_score += multiplier * bid
        multiplier += 1
    
    print(colored(f"The total score is: {total_score}", "light_green"))

if __name__ == "__main__":
    main()

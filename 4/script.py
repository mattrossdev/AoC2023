from functools import cache

number_winning_numbers = 10

def get_matches(card) -> int: 
    card = card.split(' ')
    numbers = []
    for i in range(len(card)): 
        if card[i].isnumeric(): 
            numbers.append(card[i])
    winning_numbers = set(numbers[0: number_winning_numbers])
    your_numbers = numbers[number_winning_numbers: len(numbers)]

    matches = 0
    for i in your_numbers: 
        if i in winning_numbers: 
            matches += 1 
    return matches

def first_problem(): 
    with open('4/input.txt', 'r') as f:
        cards = f.read().split('\n')
        total = 0 
        for card in cards: 
            num_matches = get_matches(card)
            if num_matches == 1: 
                total += 1 
            elif num_matches > 1: 
                total += 2 ** (num_matches - 1)
        
        return total

def second_problem(): 
    with open('4/input.txt', 'r') as f:
        cards = f.read().split('\n')
 
        @cache
        def process_card_tree(index) -> int: 
            num_matches = get_matches(cards[index])
            if num_matches == 0: 
                return 1
            
            total_cards = 1
            for i in range(index + 1, index + 1 + num_matches): 
                total_cards += process_card_tree(i)
            return total_cards
        
        total = 0 
        for i in range(len(cards)): 
            total += process_card_tree(i)

        return total

print(first_problem())
print(second_problem())

from collections import defaultdict
import math

max_red = 12
max_green = 13
max_blue = 14

def format_game_data(data: list[str]) -> list[str]: 
    formatted_data = []
    for i in range(len(data)): 
        new = data[i].split(':')
        new = new[1]
        new = new.replace(';', ',')
        new = new.strip('')
        new = new.split(',')
        formatted_data.append(new)
    return formatted_data

def get_color(s: str) -> str: 
    if 'red' in s: 
        return 'red'
    elif 'green' in s:
        return 'green'
    else:
        return 'blue'

def is_valid_game(game: list[str]) -> bool:
    for i in range(len(game)): 
        color = get_color(game[i])
        count = int(game[i].split(' ')[1]) 
        if color == 'red' and count > max_red:
            return False
        elif color == 'green' and count > max_green: 
            return False
        elif color == 'blue' and count > max_blue: 
            return False
    
    return True

def max_colors_product(game: list[str]) -> bool: 
    max_colors = defaultdict(int)

    for i in range(len(game)): 
        color = get_color(game[i])
        count = int(game[i].split(' ')[1])
        max_colors[color] = max(max_colors[color], count)
    
    return math.prod(max_colors.values())

def first_problem(): 
    with open('2/input.txt', 'r') as f:
        lines = f.read().split('\n')
        formatted_data = format_game_data(lines)
        valid_game_ids = []
        for i in range(len(formatted_data)): 
            game = formatted_data[i]
            if is_valid_game(game):
                valid_game_ids.append(i + 1)
    return sum(valid_game_ids)

def second_problem(): 
    with open('2/input.txt', 'r') as f:
        lines = f.read().split('\n')
        formatted_data = format_game_data(lines)
        total_powers = 0 
        for i in range(len(formatted_data)): 
            game = formatted_data[i]
            total_powers += max_colors_product(game)
    return total_powers

print(first_problem())
print(second_problem())




from collections import defaultdict

lines = open('3/input.txt', 'r').read().splitlines()
rows = len(lines)
cols = len(lines[0])

# Directions to check adjacent cells
directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

def is_symbol(s: str) -> bool: 
    return not s.isalnum() and s != '.'

def first_problem(): 
    total = 0 
    for i in range(rows): 
        current_num = ''
        is_part_number = False
        for j in range(cols): 
            if lines[i][j].isnumeric(): 
                current_num += lines[i][j]
                if not is_part_number:
                    for dir_i, dir_j in directions: 
                        new_i, new_j = i + dir_i, j + dir_j
                        if 0 <= new_i < rows and 0 <= new_j < cols and is_symbol(lines[new_i][new_j]): 
                            is_part_number = True 
                
                if j == cols - 1 and current_num and is_part_number: 
                    total += int(current_num)
                    current_num = ''
                    is_part_number = False
            
            elif not lines[i][j].isnumeric() and current_num: 
                if is_part_number: 
                    total += int(current_num)
                
                current_num = '' 
                is_part_number = False
    
    return total

def second_problem(): 
    gear_positions = []
    for i in range(rows): 
        for j in range(cols): 
            if lines[i][j] == '*': 
                gear_positions.append((i, j))
    
    gear_parts = defaultdict(list)
    total = 0

    for i,j in gear_positions: 
        seen = set()
        for dir_i, dir_j in directions: 
            new_i, new_j = i+ dir_i, j + dir_j
            if 0 <= new_i < rows and 0 <= new_j < cols and lines[new_i][new_j].isnumeric(): 
                while new_j >= 1 and lines[new_i][new_j - 1].isnumeric(): 
                    new_j -= 1 
                if ((new_i, new_j)) not in seen:
                    num = lines[new_i][new_j]
                    seen.add((new_i, new_j))
                    while new_j < cols - 1 and lines[new_i][new_j + 1].isnumeric(): 
                        new_j += 1 
                        num += lines[new_i][new_j]
                    gear_parts[(i,j)].append(num)
    for i in gear_parts.values(): 
        if len(i) == 2: 
            total += int(i[0]) * int(i[1])
    return total

print(first_problem())
print(second_problem())








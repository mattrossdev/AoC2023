def get_start_number(s: str) -> int:
    for i in s: 
        if i.isnumeric(): 
            return i 
    return False

def get_end_number(s: str) -> int: 
    for i in range(len(s) - 1, -1, -1): 
        if s[i].isnumeric(): 
            return s[i]
    return False

def first_problem(): 
    with open('1/input.txt', 'r') as f:
        lines = f.read().split('\n')
        total = 0 
        for i in lines: 
            start = get_start_number(i)
            end = get_end_number(i)
            num = start + end
            total += int(num)
        return total

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def get_start_number_or_digit(s: str) -> int: 
    for i in range(len(s)): 
        if s[i].isnumeric(): 
            start_number = s[i]
            start_number_index = i
            break
    
    start_digit = None
    start_digit_index = float('inf') 
    for i in digits:
        if i in s: 
            current_index = s.index(i)
            if current_index < start_digit_index: 
                start_digit = i 
                start_digit_index = current_index
    
    if start_number_index < start_digit_index: 
        return start_number
    else: 
        return digits[start_digit]


def get_end_number_or_digit(s: str) -> int: 
    end_number = None
    end_number_index = -float('inf')
    for i in range(len(s)): 
        if s[i].isnumeric(): 
            end_number = s[i]
            end_number_index = i
    
    end_digit = None
    end_digit_index = -float('inf')
    for i in digits: 
        if i in s: 
            current_index = s.rindex(i)
            if current_index > end_digit_index: 
                end_digit = i
                end_digit_index = current_index
    
    if end_number_index > end_digit_index: 
        return end_number
    else: 
        return digits[end_digit]

def second_problem(): 
    with open('1/input.txt', 'r') as f:
        lines = f.read().split('\n')
        total = 0 
        for i in lines: 
            start = get_start_number_or_digit(i)
            end = get_end_number_or_digit(i)
            num = start + end 
            total += int(num) 
        return total

print(first_problem())
print(second_problem())

            






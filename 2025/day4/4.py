##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.rstrip('\n') for line in file.readlines()]
    return data


def accessible_rolls(data):
    num_rows = len(data)
    num_cols = len(data[0])

    adjacent_positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    accessible_rolls = 0
    for i in range(0,num_rows):
        for j in range(0,num_cols):
            adjacent_rolls = 0
                    
            if data[i][j] == '@':
                for delta_row, delta_col in adjacent_positions:
                    check_i, check_j = i + delta_row, j + delta_col #new adjacent position to check
                    if 0 <= check_i < num_rows and 0 <= check_j < num_cols: #ensure our index to check exists within the data
                        if data[check_i][check_j] == '@':
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls

data = get_data('input4.txt')
ans1 = accessible_rolls(data)
print(f'Part 1 answer: {ans1}') #1505

##part 2
def removable_rolls(data):
    num_rows = len(data)
    num_cols = len(data[0])

    adjacent_positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    removed_rolls = 0

    while True:
        cycle_removal = 0
        for i in range(0,num_rows):
            for j in range(0,num_cols):
                adjacent_rolls = 0
                        
                if data[i][j] == '@':
                    for delta_row, delta_col in adjacent_positions:
                        check_i, check_j = i + delta_row, j + delta_col #new adjacent position to check
                        if 0 <= check_i < num_rows and 0 <= check_j < num_cols: #ensure our index to check exists within the data
                            if data[check_i][check_j] == '@':
                                adjacent_rolls += 1

                    if adjacent_rolls < 4:
                        #data is a list of strings, so alter entire row by changing the jth element
                        data[i] = data[i][:j] + '.' + data[i][j+1:]
                        removed_rolls += 1
                        cycle_removal += 1
                        
        if cycle_removal == 0:
            break

    return removed_rolls

ans2 = removable_rolls(data)
print(f'Part 2 answer: {ans2}') #9182

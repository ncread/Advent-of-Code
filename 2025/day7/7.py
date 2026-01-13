##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [list(line.rstrip('\n')) for line in file.readlines()]
    return data


def initialize_beam(data): #establish the initial tachyon beam x-coordinate
    s_index = data[0].index('S')
    for i in range(1,len(data)):
        if data[i][s_index] != '^':
            data[i][s_index] = '|'
        else:
            break_point = i
            break
    return break_point


def beam_splits(breakpoint, data):
    splits = 0

    for i in range(breakpoint,len(data)):
        for j in range(0,len(data[0])):
            if data[i-1][j] == '|':
                if data[i][j] == '^':
                    data[i][j-1] = '|'
                    data[i][j+1] = '|'
                    splits += 1
                elif data[i][j] == '.':
                    data[i][j] = '|'
    return splits

data = get_data('input7.txt')
breakpoint = initialize_beam(data)
ans1 = beam_splits(breakpoint, data)
print(f'Part 1 answer: {ans1}') #1649


##part 2
def quantum_tachyon(data):
    end_position_list = [0] * len(data[0])
    s_index = data[0].index('S')
    end_position_list[s_index] = 1
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data [i][j] == '^':
                #for each j index with ^, add value at j (possible timelines) to left and right
                end_position_list[j-1] += end_position_list[j]
                end_position_list[j+1] += end_position_list[j]
                end_position_list[j] = 0 #set the index of j back to zero

    return sum(end_position_list)

ans2 = quantum_tachyon(data)
print(f'Part 2 answer: {ans2}') #16937871060075
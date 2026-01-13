##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return data


def get_password(data):
    zero_count = 0
    position = 50

    for i in data:
        rotation = i.strip()

        #if L, subtract the number from position. If R, add number to position
        if 'L' in rotation:
            position -= int(rotation[1:])
        elif 'R' in rotation:
            position += int(rotation[1:])

        #if position hits either 0 or a multiple of 100 (acts as zero here since dial is a circle), we count it as a zero
        if position == 0 or position % 100 == 0:
            zero_count += 1
    return zero_count


data = get_data('input1.txt')
ans1 = get_password(data)
print(f'Part 1 answer: {ans1}') #1040

##part2
def passing_zero(data):
    zero_count = 0
    position = 50

    for i in data:
        rotation = i.strip()
        
        if 'L' in rotation:
            #increment the position by 1 and check if it's zero or multiple of 100 every time
            for i in range(1,int(rotation[1:])+1):
                position -= 1
                if position == 0 or position % 100 == 0:
                    zero_count += 1

        elif 'R' in rotation:
            for i in range(1,int(rotation[1:])+1):
                position += 1
                if position == 0 or position % 100 == 0:
                    zero_count += 1
    return zero_count


ans2 = passing_zero(data)
print(f'Part 2 answer: {ans2}') #6027
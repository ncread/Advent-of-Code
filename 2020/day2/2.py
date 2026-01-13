import re

def get_data(input_file):
    delimiters = r'[-:\s]+'

    with open(input_file, "r") as file:
        data = [line.strip('\n') for line in file.readlines()]
        data = [re.split(delimiters, item) for item in data] #split by dash, colon and spaces
    return data


def get_validpw(data):
    valid_pw = 0

    for i in data:
        low_range = int(i[0])
        high_range = int(i[1])

        if low_range <= i[3].count(i[2]) <= high_range:
            valid_pw += 1

    return valid_pw

data = get_data("input2.txt")
ans1 = get_validpw(data)
print(f'Part 1 answer: {ans1}') #655

##part 2
def part2_pw(data):
    valid_pw = 0
    matches = 0

    for i in data:
        ind1 = int(i[0])-1
        ind2 = int(i[1])-1

        if (i[3][ind1] == i[2]) != (i[3][ind2] == i[2]):
            valid_pw += 1
        
    return valid_pw


ans2 = part2_pw(data)
print(f'Part 2 answer: {ans2}') #673
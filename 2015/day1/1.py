##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.readline()
    return data


def end_floor(data):
    floor = 0
    for i in data:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
    return floor
    

data = get_data("input1.txt")
ans1 = end_floor(data)
print(f'Part 1 answer: {ans1}') #138


##part 2
def basement_index(data):
    floor = 0
    for i in range(0,len(data)):
        if data[i] == '(':
            floor += 1
        elif data[i] == ')':
            floor -= 1
        
        if floor == -1:
            return i+1 #questions asks for the position, not the index (index of 4 would be the 5th positioned element)


ans2 = basement_index(data)
print(f'Part 2 answer: {ans2}') #1771

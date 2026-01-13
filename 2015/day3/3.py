##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.readline()
    return data


def house_deliveries(data):
    house_coord_list = [(0,0)]

    for i in data:
        if i == '^':
            new_coord = (house_coord_list[-1][0], house_coord_list[-1][1]+1) #y-axis positive
        elif i == 'v':
            new_coord = (house_coord_list[-1][0], house_coord_list[-1][1]-1) #y-axis negative
        elif i == '>':
            new_coord = (house_coord_list[-1][0]+1, house_coord_list[-1][1]) #x-axis positive
        elif i == '<':
            new_coord = (house_coord_list[-1][0]-1, house_coord_list[-1][1]) #x-axis negative
        
        house_coord_list.append(new_coord)
    
    deliveries = len(set(house_coord_list))
    return deliveries


data = get_data("input3.txt")
ans1 = house_deliveries(data)
print(f'Part 1 answer: {ans1}') #2081


##part 2
santa_coord = [(0,0)]
robot_coord = [(0,0)]

for i in range(0,len(data)):
    if i % 2 != 0:
        if data[i] == '^':
            new_coord = (santa_coord[-1][0], santa_coord[-1][1]+1) #y-axis positive
        elif data[i] == 'v':
            new_coord = (santa_coord[-1][0], santa_coord[-1][1]-1) #y-axis negative
        elif data[i] == '>':
            new_coord = (santa_coord[-1][0]+1, santa_coord[-1][1]) #x-axis positive
        elif data[i] == '<':
            new_coord = (santa_coord[-1][0]-1, santa_coord[-1][1]) #x-axis negative

        santa_coord.append(new_coord)


    elif i % 2 == 0:
        if data[i] == '^':
            new_coord = (robot_coord[-1][0], robot_coord[-1][1]+1) #y-axis positive
        elif data[i] == 'v':
            new_coord = (robot_coord[-1][0], robot_coord[-1][1]-1) #y-axis negative
        elif data[i] == '>':
            new_coord = (robot_coord[-1][0]+1, robot_coord[-1][1]) #x-axis positive
        elif data[i] == '<':
            new_coord = (robot_coord[-1][0]-1, robot_coord[-1][1]) #x-axis negative

        robot_coord.append(new_coord)

ans2 = len(set(santa_coord + robot_coord))
print(f'Part 2 answer: {ans2}') #2341
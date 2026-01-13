##part 1
def get_data(input_file: str) -> list:
    with open(input_file, "r") as file:
        data = [line.rstrip() for line in file.readlines()]
    return data


def submarine_position(data: list) -> int:
    x = 0
    y = 0

    for i in data:
        dir, num = i.split(' ') #direction, number
        match dir:
            case 'forward':
                x += int(num)
            case 'up':
                y -= int(num)
            case 'down':
                y += int(num)
    
    return x*y

data = get_data('input2.txt')
ans1 = submarine_position(data)
print(f'Part 1 answer: {ans1}') #1698735

##part 2
def aim_inclusion(data: list) -> int:
    x = 0
    y = 0
    aim = 0

    for i in data:
        dir, num = i.split(' ') #direction, number
        match dir:
            case 'forward':
                x += int(num)
                y += aim * int(num)
            case 'up':
                aim -= int(num)
            case 'down':
                aim += int(num)
    
    return x*y

ans2 = aim_inclusion(data)
print(f'Part 2 answer: {ans2}') #1594785890
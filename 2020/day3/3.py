def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.strip('\n') for line in file.readlines()]
    return data


def tree_count(data, num_x, num_y):
    x = 0
    y = 0
    xlimit = len(data[0])
    tree_count = 0

    while y < len(data)-num_y: #we increment y within the loop, so subtract # of rows you move down to not overindex
        for _ in range(num_x):
            x += 1
            if x > xlimit - 1:
                x = 0
        y += num_y
        if data[y][x] == '#':
            tree_count += 1

    return tree_count


data = get_data("input3.txt")
ans1 = tree_count(data, 3, 1)
print(f'Part 1 answer: {ans1}')

##part 2
ans2 = tree_count(data, 1, 1) * tree_count(data, 3, 1) * tree_count(data, 5, 1) * tree_count(data, 7, 1) * tree_count(data, 1, 2)
print(f'Part 2 answer: {ans2}') #3847183340
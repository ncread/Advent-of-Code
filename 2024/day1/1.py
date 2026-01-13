##part 1
def get_data(input_file):
    data = []
    with open(input_file, "r") as file:
        input = [line for line in file.readlines()]

    for line in input:
        data.append(int(line.split('   ')[0]))
        data.append(int(line.split('   ')[1]))
    return data


def total_distance(data):
    first_col = data[::2]
    second_col = data[1::2]

    first_col.sort()
    second_col.sort()

    diff = []
    for i in range(len(first_col)): #both cols are same length, so could do range(1000), range(len(first_col)) or range(len(second_col))
        diff.append(first_col[i] - second_col[i])
        abs_diff = [i*(-1) if i<0 else i for i in diff]

    return sum(abs_diff)


data = get_data('input1.txt')
ans1 = total_distance(data)
print(f'Part 1 answer: {ans1}') #1970720

##part 2
def similarity_score(data):
    sim_score = []

    first_col = data[::2]
    second_col = data[1::2]

    for i in first_col:
        count = 0
        for j in second_col:
            if i == j:
                count += 1
        sim_score.append(i * count)
    
    return sum(sim_score)


ans2 = similarity_score(data)
print(f'Part 2 answer: {ans2}') #17191599

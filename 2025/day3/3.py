##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.rstrip('\n') for line in file.readlines()]
    return data


def total_joltage(data):
    joltage_list = []

    for line in data:
        first_num = 0
        second_num = 0

        #get first digit--need to iterate through entire line up to length-1 
        for i in range(1,len(line)):
            if int(line[i-1]) > first_num:
                first_num = int(line[i-1])
                first_num_loc = int(i-1)

        #we start iterating at index right after the chosen first_num, to the end of the line
        for j in range(first_num_loc+1, len(line)):
            if int(line[j]) > second_num:
                second_num = int(line[j])
        joltage = int(str(first_num) + str(second_num))
        joltage_list.append(joltage)
    return sum(joltage_list)

data = get_data('input3.txt')
ans1 = total_joltage(data)
print(f'Part 1 answer: {ans1}') #17343

##part 2
def enhanced_joltage(data):
    joltage_list_sums = []

    for line in data:
        joltage_list = []
        needed_nums = 12
        num_loc = 0
        
        for _ in range(12):
            initial_num = 0
            for i in range(0+num_loc,len(line)-needed_nums+1):
                if int(line[i]) > initial_num:
                    num = int(line[i])
                    num_loc = i + 1
                    initial_num = num

            joltage_list.append(str(num))
            cumu_joltage = ''.join(joltage_list)
            needed_nums -= 1
            
        joltage_list_sums.append(cumu_joltage)
        joltage_list_sums = [int(joltage) for joltage in joltage_list_sums]
    return sum(joltage_list_sums)

ans2 = enhanced_joltage(data)
print(f'Part 2 answer: {ans2}') #172664333119298
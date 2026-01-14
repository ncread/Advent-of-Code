##part 1
def get_data(input_file: str) -> list:
    with open(input_file, "r") as file:
        data = [line.rstrip() for line in file.readlines()]
    return data


def power_consumption(data: list) -> int:
    gamma_bin = ''
    epsilon_bin = ''

    for j in range(0,len(data[0])):
        column_nums = '' #initialize empty string for every column to hold column contents
        for i in range(0,len(data)):
            column_nums += data[i][j]
        if column_nums.count('0') > column_nums.count('1'):
            gamma_bin += '0'
            epsilon_bin += '1'
        else:
            gamma_bin += '1'
            epsilon_bin += '0'

    #converting from binary to decimal
    gamma_rate = int(gamma_bin, 2)
    epsilon_rate = int(epsilon_bin, 2)

    return gamma_rate * epsilon_rate

data = get_data('input3.txt')
ans1 = power_consumption(data)
print(f'Part 1 answer: {ans1}') #2250414

##part 2
def oxygen_generator(data: list) -> int:
    o2_rating_bin = ''

    for j in range(0,len(data[0])):
        column_nums = ''

        for i in range(0,len(data)):
            column_nums += data[i][j]

        if column_nums.count('0') > column_nums.count('1'):
            o2_rating_bin += '0'
            keep_indices = [index for index,value in enumerate(column_nums) if value == '0']
            data = [row for index, row in enumerate(data) if index in keep_indices]
        else: 
            o2_rating_bin += '1'
            keep_indices = [index for index,value in enumerate(column_nums) if value == '1']
            data = [row for index, row in enumerate(data) if index in keep_indices]
    o2_rating = int(o2_rating_bin, 2)

    return o2_rating


def co2_scrubber(data: list) -> int:
    co2_rating_bin = ''

    for j in range(0,len(data[0])):
        column_nums = ''

        for i in range(0,len(data)):
            column_nums += data[i][j]

        if column_nums.count('0') > column_nums.count('1'):
            co2_rating_bin += '1'
            keep_indices = [i for i,x in enumerate(column_nums) if x == '1']
            data = [row for index, row in enumerate(data) if index in keep_indices]
        else: 
            co2_rating_bin += '0'
            keep_indices = [i for i,x in enumerate(column_nums) if x == '0']
            data = [row for index, row in enumerate(data) if index in keep_indices]
        
        '''if only one line from the original data remains, the rest of those numbers are kept rather than
        the less frequent one (which would yield the wrong number once one line in data remains)'''
        if len(data) == 1:
            co2_rating_bin = data[0]
            break
    co2_rating = int(co2_rating_bin, 2)

    return co2_rating

o2_rating = oxygen_generator(data)
co2_rating = co2_scrubber(data)
ans2 = o2_rating * co2_rating
print(f'Part 2 answer: {ans2}') #6085575
##part 1
def get_data(input_file):
    with open("input2.txt", "r") as file:
        data = file.readline().split(',')

    data_str = [tuple(i.split('-')) for i in data]
    data_tup = [tuple(int(i) for i in tup) for tup in data_str]

    return data_tup


def invalid_id(data):
    invalid_id_list = []

    for tup in data:
        seq_start = tup[0]
        seq_end = tup[1]
        current = seq_start

        for i in range((seq_end - seq_start)+1): #loop through number of times equal to number of numbers in the tuple (inclusive)
            num_len = len(str(current))
            half_len = num_len//2
            if num_len % 2 == 0:
                first_half = str(current)[0:half_len]
                second_half = str(current)[half_len:]
                if first_half == second_half:
                    invalid_id_list.append(current)
            current += 1
    return sum(invalid_id_list)

data = get_data('input2.txt')
ans1 = invalid_id(data)
print(f'Part 1 answer: {ans1}') #38437576669

##part 2
def repeating_id(data):
    invalid_id_list = []

    for tup in data:
        seq_start = tup[0]
        seq_end = tup[1]
        current = seq_start

        for i in range((seq_end - seq_start)+1):
            num_len = len(str(current))
            #if number is more than 1 digit, but a set of the number as a string is 1, that means all digits of the number are the same (hence an invalid id)
            if num_len > 1 and len(set(str(current))) == 1:
                invalid_id_list.append(current)
                current += 1
                continue #we need to skip the rest of the loop to avoid counting the instance twice if this condition is met (plus another below)
            
            #brute force checking number of digits in current number, seeing if it repeats any sets of digits (ex. does a 9 digit number repeat a 3 number sequence 3 times)
            if num_len == 4 and str(current)[:2] == str(current)[2:]:
                invalid_id_list.append(current)
            if num_len == 6 and ( (str(current)[:2] == str(current)[2:4] == str(current)[4:]) or (str(current)[:3] == str(current)[3:]) ):
                invalid_id_list.append(current)
            if num_len == 8 and ( (str(current)[:2] == str(current)[2:4] == str(current)[4:6] == str(current)[6:]) or (str(current)[:4] == str(current)[4:]) ):
                invalid_id_list.append(current)
            if num_len == 9 and (str(current)[:3] == str(current)[3:6] == str(current)[6:]):
                invalid_id_list.append(current)
            if num_len == 10 and ( (str(current)[:2] == str(current)[2:4] == str(current)[4:6] == str(current)[6:8] == str(current)[8:]) or (str(current)[:5] == str(current)[5:]) ):
                invalid_id_list.append(current)
            current += 1
    return sum(invalid_id_list)

ans2 = repeating_id(data)
print(f'Part 2 answer: {ans2}') #49046150754
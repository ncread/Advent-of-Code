##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.strip('\n') for line in file.readlines()]
    return data


def nice_string(data):
    nice_string_count = 0

    for i in data:
        nice_criteria = 0
        vowel_count = 0
        duplicates = 0
        prohibited_pattern = 0

        for j in range(0,len(i)-1):
            if i[j] in vowels:
                vowel_count += 1
            if i[j] == i[j+1]:
                duplicates += 1
            if i[j]+i[j+1] in ['ab','cd','pq','xy']:
                prohibited_pattern += 1
                
        if i[-1] in vowels:
            vowel_count += 1
        if vowel_count >= 3:
            nice_criteria += 1
        if duplicates > 0:
            nice_criteria += 1
        if prohibited_pattern == 0:
            nice_criteria += 1

        if nice_criteria == 3:
            nice_string_count += 1
    
    return nice_string_count


vowels = 'aeiou'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

data = get_data("input5.txt")
ans1 = nice_string(data)
print(f'Part 1 answer: {ans1}')


##part 2
def nice_string_p2(data):
    nice_string_count = 0

    for i in data:
        nice_criteria = 0
        successive_set = set()
        previous_dup = ''

        for j in range(1,len(i)):
            successive_letters = i[j-1] + i[j]
            if successive_letters in successive_set and successive_letters != previous_dup:
                nice_criteria += 1
                break
            else:
                successive_set.add(successive_letters)
                previous_dup = successive_letters
        
        for k in range(1,len(i)-1):
            if i[k-1] == i[k+1]:
                nice_criteria += 1
                break
        
        if nice_criteria == 2:
            nice_string_count += 1

    return nice_string_count


ans2 = nice_string_p2(data)
print(f'Part 2 answer: {ans2}') #53

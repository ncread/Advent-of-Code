import hashlib


##part 1
def get_hash(input_string, beginning_param):
    num = 1
    while True:
        m = hashlib.md5()
        string = input_string + str(num)
        m.update(string.encode('utf-8'))
        hash = m.hexdigest()

        if hash[:len(beginning_param)] != beginning_param:
            num += 1
            continue
        else:
            return num


input = 'yzbqklnj'
part1_beginning = '00000'
        
ans1 = get_hash(input, part1_beginning)
print(f'Part 1 answer: {ans1}') #282749


##part 2
part2_beginning = '000000'
ans2 = get_hash(input, part2_beginning)
print(f'Part 2 answer: {ans2}') #9962624
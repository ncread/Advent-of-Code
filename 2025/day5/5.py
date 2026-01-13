##part 1
def get_data(input_file):
    with open("input5.txt", "r") as file:
        data = [line.rstrip('\n') for line in file.readlines()]
    return data


def transform_data(data):
    fresh = []
    available = []

    for line in data:
        if '-' in line:
            tup = tuple(line.split('-'))
            int_tup = tuple(map(int, tup))
            fresh.append(int_tup)
        else:
            available.append(line)
    
    del available[0] #empty line
    available = [int(elem) for elem in available]
    return fresh, available


def fresh_ids(fresh, available):
    total = 0

    for i in available:
        for j in fresh:
            if j[0] <= i <= j[1]:
                total += 1
                break #avoid counting an ID numerous times if it falls in numerous ranges
    return total

data = get_data('input5.txt')
fresh, available = transform_data(data)
ans1 = fresh_ids(fresh, available)
print(f'Part 1 answer: {ans1}') #525

##part 2
def compute_ids(fresh):
    fresh.sort() #sorts by 1st number in each element
    fresh = [list(i) for i  in fresh] #need to convert to lists rather than tuples for mutability
    new_ranges = [fresh[0]] #automatically start with the first range

    for i in fresh[1:]: #starting at 2nd range
        if i[0] <= new_ranges[-1][1]: #compares 1st num in range to 2nd num of previous range
            new_ranges[-1][1] = max(new_ranges[-1][1], i[1]) 
        else:
            new_ranges.append(i) #if ranges dont overlap, add entire new range to list 

    #now we can compute the difference of each range and take sum
    total_fresh = 0
    for i in new_ranges:
        diff = i[1]-i[0]+1
        total_fresh += diff
    
    return total_fresh

ans2 = compute_ids(fresh)
print(f'Part 2 answer: {ans2}') #333892124923577
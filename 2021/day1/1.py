##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.strip('\n') for line in file.readlines()]
        data = [int(num) for num in data]
    return data

def count_increases(data):
    count = 0
    for i in range(0,len(data)-1):
        if data[i+1] > data[i]:
            count += 1
    return count

data = get_data("input1.txt")
ans1 = count_increases(data)
print(f'Part 1 answer: {ans1}') #1655

##Part 2
def sum_increases(data):
    count = 0
    prev_sum = sum(data[:3]) #initialize comparison sum
    for i in range(3,len(data)):
        comparison_sum = sum(data[i:i-3:-1]) #current num, plus previous two
        if comparison_sum > prev_sum:
            count += 1
        prev_sum = comparison_sum
    return count

ans2 = sum_increases(data)
print(f'Part 2 answer: {ans2}') #1683
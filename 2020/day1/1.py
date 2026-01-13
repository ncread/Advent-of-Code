##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [int(line.strip('\n')) for line in file.readlines()]
    return data


def find_two_entries(data, target):
    s = set() #represents numbers that we've "already seen" as we continue through our single loop
    for i in data:
        complement = target - i
        if complement in s: #check if we've already seen the current number's complement (if it's in our set)
            return i * complement
        s.add(i)


data = get_data("input1.txt")
ans1 = find_two_entries(data, 2020)
print(f'Part 1 answer: {ans1}') #972576


##part 2
def find_three_entries(data, target):
    data = sorted(data)
    n = len(data)

    for i in range(0, n-2):
        left = i+1
        right = n-1

        while left < right: #perform this for each i up until left and right converge, then we move on to next i
            sum = data[i] + data[left] + data[right]

            if sum == target:
                return data[i] * data[left] * data[right]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1

    return None


ans2 = find_three_entries(data, 2020)
print(f'Part 2 answer: {ans2}') #199300880
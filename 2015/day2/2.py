import math

##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.strip('\n').split('x') for line in file.readlines()]
    
    data = [[int(el) for el in sublist] for sublist in data]
    return data


def get_paper_req(data):
    paper_needed = 0

    for i in data:
        #2*l*w + 2*w*h + 2*h*l
        surface_area = (2*i[0]*i[1]) + (2*i[1]*i[2]) + (2*i[0]*i[2])
        extra_paper = min((i[0]*i[1]), (i[1]*i[2]), (i[0]*i[2]))

        present_paper = surface_area + extra_paper
        paper_needed += present_paper
    
    return paper_needed


data = get_data("input2.txt")
ans1 = get_paper_req(data)
print(f'Part 1 answer: {ans1}') #1598415


##part 2
def get_ribbon(data):
    ribbon_needed = 0

    for i in data:
        ribbon_len = (2*sorted(i)[0]) + (2*sorted(i)[1])
        bow_len = math.prod(i)

        present_ribbon = ribbon_len + bow_len
        ribbon_needed += present_ribbon
    
    return ribbon_needed


ans2 = get_ribbon(data)
print(f'Part 2 answer: {ans2}') #3812909
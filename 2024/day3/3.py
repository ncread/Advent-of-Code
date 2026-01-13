##part 1
import re

def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    return data


def get_mul_sequences(data):
    #find the 'mul(number,number)' elements in the provided input
    muls = re.findall(r'mul\(\d+,\d+\)', data)
    return muls


def muls_sum(muls):
    product_list = []

    for i in muls:
        nums = re.findall(r'\d+', i) #extract nums from the mul(#,#) elements
        nums_int = [int(i) for i in nums]
        product_list.append(nums_int[0] * nums_int[1])

    return sum(product_list)


data = get_data("input3.txt")
muls = get_mul_sequences(data)
ans1 = muls_sum(muls)
print(f'Part 1 answer: {ans1}') #178538786

##part 2
def get_mul_indices(data):
    mul_list = []

    mul_matches = re.finditer(r'mul\(\d+,\d+\)', data)
    for mul in mul_matches:
        mul_list.append(mul.start())
    return mul_list


def get_indices(substring, string):
    #returns list of indices where the given substring starts in given string
    loc_list = []
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        loc_list.append(index)
        start_index = index+1
    return loc_list



def enabled_sums(data):
    viable_mul_list = []
    flag = 1 #any mul(#,#) instance before any do() or don't() counts per instructions
    for i in range(0,len(data)):
        if i in do_list:
            flag = 1 #set flag as 1 if we hit a do()
        elif i in dont_list:
            flag = 0 #set flag as 0 if we hit a don't()
        if i in mul_list and flag == 1: 
            #flag needs to be 1 AND we must hit the beginning of a mul() in the input
            #we notate if the mul() is safe and grab its index
            viable_mul_list.append(mul_list.index(i)) 

    new_prod_list = []
    #loop through the safe mul()s and extract their numbers to calculate a product, then sum them all to retrieve our answer
    for i in viable_mul_list:
        nums = re.findall(r'\d+', muls[i])
        nums_int = [int(i) for i in nums]
        new_prod_list.append(nums_int[0] * nums_int[1])
    
    return sum(new_prod_list)


do_list = get_indices('do()', data)
dont_list = get_indices('don\'t()', data)
mul_list = get_mul_indices(data)

ans2 = enabled_sums(data)
print(f'Part 2 answer: {ans2}') #102467299
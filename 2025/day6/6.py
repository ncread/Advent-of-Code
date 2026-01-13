import math

##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.rstrip('\n') for line in file.readlines()]
    return data


def transform_data(data):
    operands = data[:-1]
    for i in range(0,len(operands)):
        operands[i] = operands[i].split()
        operands[i] = [int(elem) for elem in operands[i]]
    operators = data[-1].split()

    return operands, operators


def grand_total(operands, operators):
    column_calcs = []
    for j in range(0,len(operators)): #columns
        nums = []
        for i in range(0,len(operands)): #numeric rows
            col_operator = operators[j]
            nums.append(operands[i][j])   
        column_calcs.append(math.prod(nums)) if col_operator == '*' else column_calcs.append(sum(nums))

    return sum(column_calcs)

data = get_data('input6.txt') #3736 cols, 5 rows w/ operator in last
operands, operators = transform_data(data) #separating & formatting numbers (operands) and operators
ans1 = grand_total(operands, operators)
print(f'Part 1 answer: {ans1}') #4583860641327

##part 2
def cephalopod_math(data):
    operators = list(data[-1]) #operator symbols
    operands = data[:-1] #numbers

    grand_total = 0
    chunk_list = []

    for j in range(len(operators)-1,-1,-1): #columns end to beginning
        column_numbers = []
        for i in range(0,len(operands)): #rows
            if operands[i][j] != ' ':
                column_numbers.append(operands[i][j])
        if len(column_numbers) > 0: #column_numbers could be empty list as chunks have column of spaces between them in the raw data
            column_result = int(''.join(column_numbers))
            chunk_list.append(column_result)
            if operators[j] != ' ':
                delta = math.prod(chunk_list) if operators[j] == '*' else sum(chunk_list)
                grand_total += delta
                chunk_list = []

    return grand_total

ans2 = cephalopod_math(data)
print(f'Part 2 answer: {ans2}') #11602774058280
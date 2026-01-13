##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = [line.strip('\n') for line in file.readlines()]

    report_nums = []
    for report in data:
        split_nums = report.split(' ')
        split_ints = [int(num) for num in split_nums]
        report_nums.append(split_ints)
    
    return report_nums


def safe_reports(data):
    safe_count = 0
    for report in data:
        inc_flag = 0
        dec_flag = 0

        for i in range(1,len(report)):
            #checks if sequence is decreasing and changes are less than 4
            if report[i-1] > report[i] and report[i-1]-report[i] < 4:
                dec_flag +=1
            #checks if sequence is increasing and changes are less than 4
            elif report[i-1] < report[i] and report[i-1]-report[i] > -4:
                inc_flag +=1
            else:
                break #if conditions aren't met, current report isn't safe
        
        #if flag is equal to length of list-1, we increment safe_count to make that entire list of nums safe 
        if dec_flag == len(report)-1 or inc_flag == len(report)-1:
            safe_count +=1
    
    return safe_count

data = get_data('input2.txt')
ans1 = safe_reports(data)
print(f'Part 1 answer: {ans1}') #402


##part 2

# #start with a function (basically same as above code) that returns True if row is safe, else False
def safety_check(report):
    inc_flag = 0
    dec_flag = 0
    #loop through each number within each list
    for i in range(1,len(report)):
        #checks if sequence is decreasing and changes are less than 4
        if report[i-1] > report[i] and report[i-1]-report[i] < 4:
            dec_flag +=1
        #checks if sequence is increasing and changes are less than 4
        elif report[i-1] < report[i] and report[i-1]-report[i] > -4:
            inc_flag +=1
        else:
            #if conditions aren't met, flag set to 0
            dec_flag = 0
            inc_flag = 0
            break
    #flag must be incrementally increased for each number transition (length of list - 1)
    #if flag is equal to length of list-1, we increment safe_count to make that entire list of nums safe 
    if dec_flag == len(report)-1 or inc_flag == len(report)-1:
        return True
    else:
        return False
    

def problem_dampener(data):
    safe_count = 0 #reset our safe row tally
    for report in data:
        if safety_check(report) == False:
            for i in range(0,len(report)):
                sliced_report = report[:i] + report[i+1:]
                if safety_check(sliced_report) == 1:
                    safe_count += 1
                    break
                else:
                    continue
        elif safety_check(report) == 1:
            safe_count += 1

    return safe_count


ans2 = problem_dampener(data)
print(f'Part 2 answer: {ans2}') #455
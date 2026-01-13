##part 1
def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    return data.splitlines()


def xmas_appearances(data):
    count = 0
    #loop through the rows (i) and columns (j)
    #check each [i][j] index and if it's an X, check each direction for an XMAS spelling
    #we make sure we don't wrap around with the indices, so we check the [i][j] to ensure we can fit 3 more letters in each given direction
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            #vertical
            if j <= len(data[i]) - 4:
                try:
                    if data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                        count +=1
                except:
                    pass
            #vertical backwards
            if j >= 3:
                try:
                    if data[i][j] == 'X' and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
                        count +=1
                except:
                    pass
            #horizontal upwards
            if i >= 3:
                try:
                    if data[i][j] == 'X' and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
                        count +=1
                except:
                    pass
            #horizontal downwards
            if i <= len(data) - 4:
                try:
                    if data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                        count +=1
                except:
                    pass
            #diagonal up/left
            if i >= 3 and j >= 3:
                try:
                    if data[i][j] == 'X' and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
                        count +=1
                except:
                    pass
            #diagonal up/right
            if i >= 3 and j <= len(data[i]) - 4:
                try:
                    if data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
                        count +=1
                except:
                    pass
            #diagonal down/left
            if i <= len(data) - 4 and j >= 3:
                try:
                    if data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                        count +=1
                except:
                    pass
            #diagonal down/right
            if i <= len(data) - 4 and j <= len(data[i]) - 4:
                try:
                    if data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                        count +=1
                except:
                    pass
    return count

data = get_data('input4.txt')
ans1 = xmas_appearances(data)
print(f'Part 1 answer: {ans1}') #2554


##part 2
def mas_crosses(data):
    xcount = 0
    #we want to first look for the A's, but only those not in the first or last col or row since it wouldn't be the center of an X
    #so we don't include the first or last rows or cols
    for i in range(1,len(data)-1):
        for j in range(1,len(data[i])-1):
            #if we encounter an A, get the letters for it's corners
            if data[i][j] == 'A':
                tl = data[i-1][j-1]
                tr = data[i-1][j+1]
                bl = data[i+1][j-1]
                br = data[i+1][j+1]

                #concat the letters to get the diagonals
                diag1 = tl + 'A' + br
                diag2 = tr + 'A' + bl

                #check if the two diagonals are 'MAS' or 'SAM'
                if diag1 in ('MAS','SAM') and diag2 in ('MAS','SAM'):
                    xcount += 1
    return xcount

ans2 = mas_crosses(data)
print(f'Part 2 answer: {ans2}') #1916
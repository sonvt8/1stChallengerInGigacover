# Line 00 is the number of rows N.
# Line 01 to N, each line contains an integer as a claim count.
# Write C code to print to output file N rows; each row i shows either 1 or 0
# where the value is
# 0--if claim_count of row i is not the maximum value of the whole list
# 1--if claim_count of row i is maximum value of the whole list
# input   output
# 4
# 0       0
# 0       0
# 2       1
# 1       0

def readFile(input):
    try:
        with open(input, mode="r") as f:
            print(f.read())
            f.seek(0,0)
            # remove newline in each lines
            return [x.rstrip('\n') for x in f.readlines()]
    except FileNotFoundError:
        print('File %s not found' % input)

def writeFile(output, lst):
    f = open(output, mode="w")
    lst.pop(0)
    maxNum = max(lst)
    i = 0
    while i < len(lst):
        f.write('1\n') if lst[i] == maxNum else f.write('0\n')
        i += 1
    f.close()

if __name__ == '__main__':
    # Read file
    content = readFile('input.txt')
    # convert string list into interger list
    results = list(map(int, content))
    # Write file
    writeFile('output.txt', results)
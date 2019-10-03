import os

def readFile(input):
    file_exists = os.path.isfile(input)
    if file_exists:
        with open(input, mode="r") as f:
            # remove newline in each lines
            return [x.rstrip('\n') for x in f.readlines()]
    else:
        raise Exception('File %s not found' % input)

def writeFile(output, lst):
    f = open(output, mode="w")
    if lst[0].isdigit():
        if (int(lst[0]) == 0):
            f.write(f'')
        else:
            try:
                lst_num = [int(i) for i in lst[1].split(', ')]  # convert all strings in list to integers
                max_num = max(lst_num)
                lst_num[:] = [(1 if x == max_num else 0) for x in lst_num]
                f.write(f'{str(lst_num)[1:-1]}')
            except Exception:
                raise Exception('All claim-count must be valid')
    elif (len(lst[0])==0):
        raise Exception('N must have a value')
    else:
        raise Exception('N must be an integer number')

def find_max_claim(input, output):
    # Read file
    content = readFile('input.txt')
    # Write file
    writeFile('output.txt', content)

if __name__ == '__main__':
    find_max_claim(input='input.txt', output='output.txt')

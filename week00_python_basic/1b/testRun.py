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
    if (lst[0] == ''):
        f.write('N must have a value')
    elif lst[0].isdigit():
        if (int(lst[0]) == 0):
            f.write('')
        else:
            lst_num = lst[1].split(', ')
            max_num = max(lst_num)
            print(max_num)
            i = 0
            while i < len(lst_num):
                f.write('', '.join(actorsByMovies())') if lst[i] == max_num else f.write('0\n')
                i += 1


    # lst.pop(0)
    # maxNum = max(lst)
    # i = 0
    # while i < len(lst):
    #     f.write('1\n') if lst[i] == maxNum else f.write('0\n')
    #     i += 1
    f.close()

def find_max_claim(input, output):
    # Read file
    content = readFile('input.txt')
    print(content)
    # Write file
    writeFile('output.txt', content)

if __name__ == '__main__':
    find_max_claim(input='input.txt', output='output.txt')

import os

def read_file(input):
    with open(input, mode="r") as f:
        # remove newline in each lines
        return [x.rstrip('\n') for x in f.readlines()]

def write_file(output, lst):
    f = open(output, mode="w")
    if (int(lst[0]) == 0):
        f.write(f'')                                                        #tc01
    else:
        try:
            lst_num = [int(i) for i in lst[1].split(', ')]  # convert all strings in list to integers
        except Exception:
            raise Exception('All claim-count must be valid')                #tc04a
        max_num = max(lst_num)
        lst_num[:] = [(1 if x == max_num else 0) for x in lst_num]
        #tc02
        f.write(f'{str(lst_num)[1:-1]}')

def find_max_claim(input, output):
    # Read file
    file_exists = os.path.isfile(input)
    if file_exists:
        content = read_file(input)
    else:
        raise Exception('File %s not found' % input)                        #tc00

    # Write file
    try:
        if os.stat(input).st_size == 0:
            raise Exception('Invalid input: Empty file')
        elif content[0] == '':
            print('N must have a value')                                    #tc03b
        elif len(content[0]) == 0:
            print('N is empty')                                             #tc03c
        else:
            try:
                #Try to convert N into interger if Claim-count exists
                [int(i) for i in content[0]] if (content[1] in content) else print ('Claim-count is empty')
            except Exception:
                raise Exception('N must be an integer number')              #tc03a
            write_file(output, content)
    except IndexError:
        raise Exception('Claim-count is empty')                             #tc04b

if __name__ == '__main__':
    find_max_claim(input='input.txt', output='output.txt')

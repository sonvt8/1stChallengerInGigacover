import os

def read_file(input):
    with open(input, mode="r") as f:
        # remove newline in each lines
        return [x.rstrip('\n') for x in f.readlines()]

def write_file(output, lst):
    with open(output, mode="w") as f:
        try:
            lst_num = [int(i) for i in lst[1:]]  # convert all strings in list to integers'
            max_num = max(lst_num)
            lst_num[:] = [(1 if x == max_num else 0) for x in lst_num]
            for ele in lst_num:                                                           #tc02
                f.write(f'{ele}\n')
        except Exception:
            raise Exception('All claim-count must be valid')                              #tc04a


def find_max_claim(input, output):
    # Read file
    file_exists = os.path.isfile(input)
    if file_exists:
        content = read_file(input)
    else:
        raise Exception('File %s not found' % input)                                      #tc00

    # Write file
    if os.stat(input).st_size == 0:
        raise Exception('Invalid input: Empty file')                                      #tc03c
    elif content[0] == '':
        raise Exception('N must have a value')                                            #tc03b
    else:
        try:
            #Try to convert N into interger if Claim-count exists
            if (int(content[0]) == 0):
                with open(output, mode="w") as f:
                    f.write(f'\n')                                                        #tc01
            else:
                if (content[1] != ''):
                    write_file(output, content)
        except ValueError:
            raise Exception('N must be an integer number')                                #tc03a
        except IndexError:
            raise Exception('Claim-count is empty')                                       #tc04b


if __name__ == '__main__':
    find_max_claim(input='input.txt', output='output.txt')

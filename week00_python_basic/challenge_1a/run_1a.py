import os

def read_file(input):
    with open(input, "r") as f:
        return [x for x in f.readline().split(', ')]

def write_file(output,lst):
    f = open(output, mode="w")
    f.write(f'{int(min(lst))}')
    f.close()

def find_min(input, output):
    # Read file
    file_exists = os.path.isfile(input)
    if file_exists:
        content = read_file(input)
    else:
        raise Exception('File %s not found' % input)                                   #tc00

    # Write file
    if os.stat(input).st_size == 0:                                                    #tc03b
        raise Exception('Invalid input: Empty file')
    elif (all('' == s or s.isspace() for s in content)):                               #tc03c
        raise Exception('Invalid input: Empty file with empty String')
    elif len(content) != 6:
        raise Exception('Invalid input: List of numbers should have 6 numbers')        #tc02
    else:
        try:
            content = [float(i) for i in content]
            write_file(output, content)                                                 #tc01
        except Exception:
            raise Exception('Invalid input: The item in the list must be a number')    #tc03a

if __name__ == '__main__':
    find_min(input='input.txt', output='output.txt')

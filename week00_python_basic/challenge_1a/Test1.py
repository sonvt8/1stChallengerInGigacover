#     Given a list of 6 float numbers from input file, print by C code to output file the minimum value of the list.
#     Sample input+output files
#     input
#     -3 -1.2 0 0 4.56 78.9
#     output
#     -3
import os
import sys

def readFile(input):
    file_exists = os.path.isfile(input)
    if file_exists:
        with open(input, "r") as f:
            return f.read().split(',')
    else:
        raise Exception('File %s not found' % input)

def writeFile(output,lst):
    f = open(output, mode="w")
    #region try to convert to float
    for i in range(0, len(lst)):
        try:
            _ = float(lst[i])
        except Exception:
            raise Exception('Invalid input: The item in the list must be a number')
    #endregion
    f.write(f'{int(min(lst))}')
    f.close()

def find_min(input, output):
    # Read file
    content = readFile(input)
    # Write file
    if (os.stat(input).st_size == 0):
        raise Exception('Invalid input: Empty file')
    elif len(content) != 6:
        raise Exception('Invalid input: List of numbers should have 6 numbers')
    else:
        writeFile(output, content)

if __name__ == '__main__':
    find_min(input='input.txt', output='output.txt')

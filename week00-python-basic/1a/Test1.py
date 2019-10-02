#     Given a list of 6 float numbers from input file, print by C code to output file the minimum value of the list.
#     Sample input+output files
#     input
#     -3 -1.2 0 0 4.56 78.9
#     output
#     -3
import os
import sys, traceback

def readFile(input):
    file_exists = os.path.isfile('input.txt')
    if file_exists:
        with open(input, "r") as f:
            return f.read().split(',')
    else:
        print('File %s not found' % input)
        sys.exit(1)

def writeFile(output,lst):
    f = open(output, mode="w")
    for i in range(0, len(lst)):
        try:
            content[i] = float(lst[i])
        except Exception:
            print('Invalid input: The item in the list must be a number')
            sys.exit(1)
    f.write(f'{int(min(lst))}')
    f.close()

if __name__ == '__main__':
    # Read file
    content = readFile('input.txt')
    # Write file
    if (os.stat('input.txt').st_size == 0):
        print('Invalid input: Empty file')
    elif len(content) != 6:
        print('Invalid input: List of numbers should have 6 numbers ')
    else:
        writeFile('output.txt', content)



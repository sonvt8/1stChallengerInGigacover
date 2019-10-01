#     Given a list of 6 float numbers from input file, print by C code to output file the minimum value of the list.
#     Sample input+output files
#     input
#     -3 -1.2 0 0 4.56 78.9
#     output
#     -3
import os
import sys, traceback

def readFile(input):
    try:
        f = open(input, mode="r")
        return f.read().split(',')
    except FileNotFoundError:
        print('File %s not found' % input)
    finally:
        f.close()

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
    content = readFile('input1.txt')
    # Write file
    if (os.stat('input1.txt').st_size == 0):
        print('Invalid input: Empty file')
    elif len(content) < 6:
        print('Invalid input: List of numbers should have at least 6 numbers ')
    else:
        writeFile('output1.txt', content)



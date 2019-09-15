#     Given a list of 6 float numbers from input file, print by C code to output file the minimum value of the list.
#     Sample input+output files
#     input
#     -3 -1.2 0 0 4.56 78.9
#     output
#     -3


def readFile(input):
    try:
        f = open(input, mode="r")
        return f.read().split()
    except FileNotFoundError:
        print('File %s not found' % input)
    finally:
        f.close()

def writeFile(output,lst):
    f = open(output, mode="w")
    for i in range(0, len(lst)):
        content[i] = float(lst[i])
    f.write(str(int(min(lst))))
    f.close()

if __name__ == '__main__':
    # Read file
    content = readFile('input1.txt')
    # Write file
    writeFile('output1.txt',content)


import sys
import math

def Prime_num(num):
    temp = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    lst = []

    for line in sys.stdin:
        lst.append(line.rstrip('\n'))

    int_lst = [int(i) for i in lst]

    for ele in int_lst[1:]:
        print('Prime') if Prime_num(ele) and ele > 1 else print('Not prime')




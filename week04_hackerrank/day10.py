import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    #substring after converting binary result into a string without '0b'
    sub_str = str(bin(n))[2:]

    #split the string to have the list of number '1'
    sub_str = sub_str.split('0')

    #return the longest string in the list
    max_str = max(sub_str, key=len)

    #print the result
    print(len(max_str))
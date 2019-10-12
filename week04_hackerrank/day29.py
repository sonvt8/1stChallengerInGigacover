#!/bin/python3

import math
import os
import random
import re
import sys

def max_bitwise(key,val):
    max_num = 0
    for i in range(1, key+1):
        for j in range(1,i):
            bitwise_and = i & j
            if max_num < bitwise_and < val:
                max_num = bitwise_and
                if bitwise_and == val - 1:
                    return bitwise_and
    return max_num

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_bitwise(n,k))

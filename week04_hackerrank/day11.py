import math
import os
import random
import re
import sys

def get_sum_ele(lst,row,col):
    sum = 0
    sum += lst[row][col] + lst[row][col+1] + lst[row][col+2]
    sum += lst[row+1][col+1]
    sum += lst[row+2][col] + lst[row+2][col+1] + lst[row+2][col+2]
    return sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # because -9 <= A[i][j] <=9
    max_sum = -63

    for i in range(0,len(arr[0])-2):
        for j in range(0,len(arr)-2):
            sum_ele = get_sum_ele(arr,i,j)
            max_sum = sum_ele if sum_ele > max_sum else max_sum
    print(max_sum)


#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
numberOfSwaps = 0
def swap(idx,lst):
    lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
    return lst

def arrange_num(lst,count):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            #  Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                swap(j, a)
                count += 1
        # If no elements were swapped during a traversal, array is sorted
        if (count == 0):
            break
    return count

if __name__ == '__main__':
    print(f'Array is sorted in {arrange_num(a,numberOfSwaps)} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

lst_of_lists = []

for line in sys.stdin:
    lst_of_lists.append(line.rstrip('\n'))

for ele in lst_of_lists[1:]:
    lst = list(ele)
    even_str = ''
    odd_str = ''
    for count,ele in enumerate(lst):
        if count % 2:
            even_str = even_str + ele
        else:
            odd_str = odd_str + ele
    print(f'{odd_str} {even_str}')
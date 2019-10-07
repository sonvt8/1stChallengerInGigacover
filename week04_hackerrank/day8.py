# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

lst_of_lists = []

#adding each lines into a list
for line in sys.stdin:
    lst_of_lists.append(line.rstrip('\n'))

#return how many ele in a dictionary
num_ele = int(lst_of_lists[0])

#adding ele taken from lst_of_list into a dictionary
my_phonebook = dict(ele.split(' ') for ele in lst_of_lists[1:num_ele+1])

#Looking for the key in my_phonebook(dict) and return the value
for name in lst_of_lists[num_ele+1:]:
    if name in my_phonebook.keys():
        print(f'{name}={my_phonebook.get(name)}')
    else:
        print('Not found')


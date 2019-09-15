# Write Python code to print driver info to output file, one driver per row, in the form of
# nricfin, First_name M. LAST_NAME, age, charged_amount
# where
# age --- is computed from date_of_birth and today year of 2019
# First_name --- is the first_name in camel-case aka all lower-case with 1st-letter upper-case
# M. --- is the middle_name initial aka first letter, and the dot
# LAST_NAME --- is the last_name in upper-case
# charged_amount --- is either
# * premium if the driver is MATURE i.e. AGE ABOVE 26
# * or DOUBLE of premium if the driver is NOT MATURE
# * or TRIPLE of premium if the driver has the GREATEST/MAXIMUM value of claim_count no matter what his age is

import datetime
now = datetime.datetime.now()

def readFile(input):
    try:
        with open(input, mode="r") as f:
            print(f.read())
            f.seek(0,0)
            # remove newline in each lines
            return [x.rstrip('\n') for x in f.readlines()]
    except FileNotFoundError:
        print('File %s not found' % input)

def writeFile(output, lst):
    code, doB, claims, firstName, middleName, lastName = [], [], [], [], [], []
    i, amt = 0, 500

    f = open(output, mode="w")
    for line in lst[2:]:
        arr = line.split()
        code.insert(i, arr[0])
        firstName.insert(i, arr[1])
        middleName.insert(i, arr[2])
        lastName.insert(i, arr[3])
        claims.insert(i, arr[-1])
        doB.insert(i, arr[-3].split('-')[0])

    i = 3
    letters = [word[0] for word in middleName]
    # Starting write file
    f.write(lst[0] + '\n')
    while i >= 0:
        if claims[i] == max(claims):
            amt = amt * 3
        elif (now.year-int(doB[i])) < 26:
            amt = amt * 2
        else:
            amt = 500
        f.write(code[i] + ', ' + firstName[i].capitalize() + ' ' + letters[i].upper() + '. ' + lastName[i].upper()
                + ', ' + str(now.year-int(doB[i])) + ', ' + str(amt) + '\n')
        i -= 1
        amt = 500
    f.close()

if __name__ == '__main__':
    # Read file
    content = readFile('input.txt')
    # Write file
    writeFile('output.txt', content)
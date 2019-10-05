import datetime
import os
import re
now = datetime.datetime.now()

class Driver:
    def __init__(self, code, firstName, middleName, lastName, doB, premium, claims):

        name = firstName + middleName + lastName
        # using regex to find empty string
        pattern = re.compile("['']")

        # Code validation
        if pattern.search(code):
            raise Exception('n must have a value')                               #tc05b
        elif code.isdigit():
            raise Exception('n must be a string')                                #tc05a
        else:
            self.code = code

        # Name validation
        if pattern.search(name):
            raise Exception('s must have a value')                               #tc06c
        elif not (verify(name)):
            raise Exception('s must be a string')                                #tc06a
        elif any(char.isdigit() for char in name):
            raise Exception('s must not include number')                         #tc06b
        else:
            self.firstName = firstName
            self.middleName = middleName
            self.lastName = lastName

        # Date validation
        if pattern.search(doB):
            raise Exception('d must have a value')                               #tc07b
        else:
            for ele in doB.split('-'):
                if not ele.isdigit():
                    raise Exception('d must be a date i.e. yyyy-mm-dd')          #tc07a
            self.doB = doB

        # Claims validation
        if pattern.search(claims):
            raise Exception('c must have a value')                               #tc09b
        elif not claims.isdigit():
            raise Exception('c must be a not-negative integer')                  #other validation
        elif int(claims) < 0:
            raise Exception('c must be a not-negative integer')                  #tc09a
        else:
            self.claims = claims

        # Premium validation
        if pattern.search(premium):
            raise Exception('p must have a value')                               #tc08b
        elif not premium.isdigit():
            raise Exception('p must be a positive float number')                 #other validation
        elif float(premium) < 0:
            raise Exception('p must be a positive float number')                 #tc08a
        else:
            self.premium = premium

    def getFistName(self):
        return self.firstName.capitalize()

    def getMiddleName(self):
        return self.middleName[0].upper()

    def getLastName(self):
            return self.lastName.upper()

    def getyear(self):
        return now.year - int(self.doB[0:4])

    def getPay(self, ref):
        if self.claims == ref:
            return 500 * 3
        elif Driver.getyear(self) < 26:
            return 500 * 2
        else:
            return 500


def verify(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if (regex.search(string) == None):
        return True
    else:
        return False

def read_file(input):
    with open(input, mode="r") as f:
        # remove newline in each lines
        return [x.rstrip('\n') for x in f.readlines()]

def write_file(output, lst):
    with open(output, mode="w") as f:
        lstDriver = []
        for index, line in enumerate(lst[2:]):
            info = line.split()
            driver_info = Driver(*info)
            lstDriver.append(driver_info)

        # insert claim of each person into the list
        claim_count = [person.claims for person in lstDriver]
        max_claim = max(claim_count)

        # Starting write file
        f.write(lst[0] + '\n')
        for person in lstDriver:
            f.write(
                person.code + ', ' + person.getFistName() + ' ' + person.getMiddleName() + '. ' + person.getLastName() + ', ' + str(person.getyear()) + ', ' + str(person.getPay(max_claim)) + '\n')                                     #tc01,tc02,tc03,tc04


def insurance_policies(input, output):
    # Read file
    file_exists = os.path.isfile(input)
    if file_exists:
        content = read_file(input)
    else:
        raise Exception('File %s not found' % input)

    # Write file
    if not content[1].isdigit():
        raise Exception('Number of Drivers should be a number')                  #other validation
    elif int(content[1]) == 0:
        with open(output, mode="w") as f:
            f.write(f'\n')                                                       #tc00
    else:
        write_file(output, content)

if __name__ == '__main__':
    insurance_policies(input='input.txt', output='output.txt')

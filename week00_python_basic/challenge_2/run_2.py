import datetime
now = datetime.datetime.now()

class Driver:
    def __init__(self, code, firstName, middleName, lastName, doB, premium, claims):
        self.code = code
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.doB = doB
        self.premium = premium
        self.claims = claims


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
    lstDriver = []
    f = open(output, mode="w")

    # extract information of Driver and insert each Driver into the list "lstDriver"
    for index,line in enumerate(lst[2:],start=1):
        info = line.split()
        name = "Driver{0}".format(index)
        name = Driver(*info)
        lstDriver.append(name)

    # insert claim of each person into the list
    claimCount = [person.claims for person in lstDriver]
    maxClaim = max(claimCount)

    # Starting write file
    f.write(lst[0] + '\n')
    for person in lstDriver:
        f.write(person.code + ', ' + person.getFistName() + ' ' + person.getMiddleName() + '. ' + person.getLastName()
                + ', ' + str(person.getyear()) + ', ' + str(person.getPay(maxClaim)) + '\n')
    f.close()

def insurance_policies(input, output):
    # Read file
    content = readFile(input)

    # Write file
    writeFile(output, content)

if __name__ == '__main__':
    insurance_policies(input='input.txt', output='output.txt')

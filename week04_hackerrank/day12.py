class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNumber)

    def calculate(self):
        avg_grade = sum(scores) / len(scores)
        if avg_grade >= 90:
            return 'O'
        elif avg_grade >= 80:
            return 'E'
        elif avg_grade >= 70:
            return 'A'
        elif avg_grade >= 55:
            return 'P'
        elif avg_grade >= 40:
            return 'D'
        else:
            return 'T'

if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
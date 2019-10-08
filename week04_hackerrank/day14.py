class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def computeDifference(self):
        min_num = min(a)
        max_num = max(a)
        self.maximumDifference = abs(min_num - max_num)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
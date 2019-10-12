# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Book:
    def __init__(self, date_released, date_expected):
        self.date_released = date_released.split()
        self.date_expected = date_expected.split()

    def get_fine(self):
        day_re, month_re, year_re = [int(ele) for ele in self.date_released]
        day_ex, month_ex, year_ex = [int(ele) for ele in self.date_expected]
        if (year_ex == year_re):
            if(month_ex == month_re):
                if(day_re <= day_ex):
                    return 0
                else:
                    return 15 * (day_re - day_ex)
            if month_re < month_ex:
                return 0
            else:
                return 500 * (month_re - month_ex)
        elif year_re < year_ex:
            return 0
        else:
            return 10000

if __name__ == '__main__':
    lst_of_date = []
    for line in sys.stdin:
        lst_of_date.append(line.rstrip('\n'))

    book_info = Book(*lst_of_date)
    print(book_info.get_fine())
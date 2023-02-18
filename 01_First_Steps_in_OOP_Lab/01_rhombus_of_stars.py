# Exam: 01. Rhombus of Stars
# From: First Steps in OOP - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1934#0

class Rhombus:

    def __init__(self, size):
        self.size = size
        self.result = ''

    def main(self):
        """
        Main method calling methods for upper and lower parts.
        :return: The finished rhombus.
        """
        self.upper_part()
        self.lower_part()
        return self.result

    def upper_part(self):
        """
        This method call draw_rhombus method and prepare the upper part of rhombus.
        """
        for row in range(1, self.size + 1):
            self.draw_rhombus(row)

    def lower_part(self):
        """
        This method call draw_rhombus method and prepare the lower part of rhombus.
        :return:
        """
        for row in range(self.size - 1, 0, -1):
            self.draw_rhombus(row)

    def draw_rhombus(self, row: int):
        """
        This func draws each row from rhombus.
        """
        self.result += (' ' * (self.size - row)) + ('* ' * row) + '\n'


if __name__ == '__main__':
    n = int(input())
    rhombus = Rhombus(n).main()
    print(rhombus)

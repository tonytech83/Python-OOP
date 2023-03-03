# Exam: 03. Integer
# From: Static and Class Methods - Lab
# https://judge.softuni.org/Contests/Practice/Index/2430#2

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for idx, num in enumerate(value):
            # idx + 1 == len(value) should be first
            if idx + 1 == len(value) or roman[num] >= roman[value[idx + 1]]:
                result += roman[num]
            else:
                result -= roman[num]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            return cls(int(value))
        except ValueError:
            return 'wrong type'


# Test code
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

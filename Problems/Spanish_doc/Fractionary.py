# Read an integer that indicates the number of input to read
# The input are two integers, the fist one is the numerator, and the second the denominator. print the simplified
# fraction

from fractions import Fraction
# The easy way :)


def main(x, y):
    return Fraction(x, y)


if __name__ == '__main__':
    n = int(input("N° of test >>> "))
    while n > 0:
        numerator, denominator = input("Numerator and denominator >>> ").split(", ")
        numerator, denominator = int(numerator), int(denominator)
        print(main(numerator, denominator))
        n -= 1

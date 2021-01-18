# Read an integer that indicates the number of input to read
# The input is one float, round that float to 2, and calculate the fraction of it.
from decimal import Decimal
from fractions import Fraction


def fraction(x):
    return Fraction(Decimal(str(x)))


def main():
    n = int(input("N° of test >>> "))
    while n > 0:
        decimal_number = float(input("Float number >>> "))
        decimal_number = round(decimal_number, 2)
        print(fraction(decimal_number))
        n -= 1


if __name__ == '__main__':
    main()

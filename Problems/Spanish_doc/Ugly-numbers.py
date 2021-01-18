# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
# … shows the first 11 ugly numbers. By convention, 1 is included.

# Read an integer that indicates the number of input to read
# The input are two integers, calculate how many ugly numbers are there between the two integers

class CalculateUgly:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.prime_divisors = [2, 3, 5]
        self.n_uglies = 0

    def check_ugl(self):
        for number in range(self.x, self.y + 1):
            if number % self.prime_divisors[0] == 0 or number % self.prime_divisors[1] == 0 or number % self.prime_divisors[2] == 0:
                self.n_uglies += 1


def main():
    n = int(input("Number of test >>> "))
    while n > 0:
        number1, number2 = input("Pair of numbers >>> ").split(", ")
        x, y = int(number1), int(number2)

        if x > y:
            check = CalculateUgly(y, x)
            check.check_ugl()
            print(check.n_uglies)
        else:
            check = CalculateUgly(x, y)
            check.check_ugl()
            print(check.n_uglies)

        n -= 1

# PD this is one of the most difficult


if __name__ == '__main__':
    main()

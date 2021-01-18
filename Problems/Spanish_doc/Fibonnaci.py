
"""
Fibonacci program
Read an input that determinates the number of Fibonacci numbers to calculate.
Calculate Fibonacci
"""


class Fibonacci:

    """Returns nth Fibonacci number. """

    def __init__(self):
        pass

    # Max nth number allowed 1000
    def get_fibonacci(self, n_position):
        if 0 == n_position or 1 == n_position:
            return 1
        elif -1 == n_position:
            return 0
        elif -1 > n_position:
            return "Negative number"
        return self.get_fibonacci(n_position - 1) + self.get_fibonacci(n_position - 2)


def main():
    try:
        n = int(input("Number of calculations > "))
        while n > 0:
            fibonacci_lenght = int(input("Nth Fibonacci number > "))
            my_Fibonacci = Fibonacci()
            print(my_Fibonacci.get_fibonacci(fibonacci_lenght - 1))
            n -= 1
    except ValueError:
        print("Fibonacci must be a number")
        main()


if __name__ == "__main__":
    main()

# Read pairs of integers until both == 0, and print prime numbers between the pair of integers.

def check_primes(number1, number2):
    number_of_primes = 0
    for i in range(number1, number2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                number_of_primes += 1

    return number_of_primes


def main():
    # Pairs separated by a comma
    while 1:
        number1, number2 = input("Pairs >>> ").split(",")
        x = int(number1)
        y = int(number2)

        if x == 0 and y == 0:
            print("Bye")
            break
        elif x < y:
            print(check_primes(x, y))
        elif x > y:
            print(check_primes(y, x))


if __name__ == '__main__':
    main()

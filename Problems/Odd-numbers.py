# Read  pairs of numbers, and print the odd numbers between these numbers. Read the pairs until input == o, o

def check_odd_numbers(x, y):
    odd_numbers = []
    for i in range(x, y + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


def main():
    # Pairs separated by a comma
    while 1:
        number1, number2 = input("Pairs >>> ").split(",")
        x = int(number1)
        y = int(number2)
        if x == 0 and y == 0:
            print("Program finished")
            break
        my_odd = check_odd_numbers(x, y)
        for i in my_odd:
            print(i)


if __name__ == '__main__':
    main()
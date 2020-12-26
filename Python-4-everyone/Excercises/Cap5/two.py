"""
Program that read numbers until the user type 'done'
and print the min and max value
"""


def main():
    useful_variable = 1
    numbers = []

    while useful_variable != 'done':
        n = input("Enter a number: ")
        if n == 'done':
            useful_variable = n

        try:
            n = int(n)
        except ValueError:
            print("Input should be an integer")
            continue

        numbers.append(n)

    if numbers:
        print('min: ', min(numbers))
        print('max: ', max(numbers))
    else:
        print('No numbers have been registered')


if __name__ == "__main__":
    main()

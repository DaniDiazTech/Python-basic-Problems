"""
Program that read numbers until the user type 'done' and print the total, count, and average of the
numbers
"""


def main():
    useful_variable = 1
    numbers = []

    while useful_variable != 'done':
        n = input("Enter a number: ")

        if n == 'done':
            useful_variable = n
        else:
            try:
                n = int(n)
            except ValueError:
                print("Input should be an integer")
                continue

            numbers.append(n)

    if numbers:
        print('total: ', sum(numbers))
        print('count: ', len(numbers))
        print('average: ', sum(numbers) / len(numbers))
    else:
        print('No numbers have been registered')


if __name__ == "__main__":
    main()

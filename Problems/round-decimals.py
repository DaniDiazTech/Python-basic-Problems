# Read a integer n, it indicates the number of test you have to do. Read n times a pair of an integer and a float
# numbers and round the float to the first integer

def main():

    n = int(input("Number of tests >>> "))
    rounded_numbers = []
    while n > 0:
        x, y = input("Integer and Float number  >>> ").split(", ")
        integer = int(x)
        float_number = float(y)
        rounded_numbers.append(round(float_number, integer))

        n -= 1

    for i in rounded_numbers:
        print(i)


if __name__ == '__main__':
    main()

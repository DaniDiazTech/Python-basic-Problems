# Read a integer n, it indicates the number of test you have to do. Read n times float numbers and calculate the average


def main():

    n = int(input("Number of tests >>> "))
    avg = []
    while n > 0:
        avg.append(float(input("Float number  >>> ")))
        n -= 1

    print(round(sum(avg) / len(avg), 4))


if __name__ == '__main__':
    main()

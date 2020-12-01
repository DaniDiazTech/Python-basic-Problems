# Read an integer that indicates the number of input to read
# The input are 3 float numbers, calculate the mean and median.

def mean(*args):
    for i in *args:


def median(*args):
    pass


def main():
    n = int(input("N° of test >>> "))
    while n > 0:
        x, y, z = input("Float number >>> ").split()

        print(f"Mode is {mean(x, y, z)}")
        print(f"Median is {median(x, y, z)}")

        n -= 1


if __name__ == '__main__':
    main()

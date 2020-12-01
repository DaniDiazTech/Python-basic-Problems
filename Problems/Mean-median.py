# Read an integer that indicates the number of input to read
# The input are 3 float numbers, calculate the mean and median.

def mean(*args):
    """
    Calculates the mean of a list of numbers
    :param args: List of numbers
    :return:  The mean of a list of numbers
    """
    index = 0
    sum_index = 0
    for i in args:
        index += 1
        sum_index += float(i)

    return (sum_index / index) if index != 0 else "Division by zero"


def median(*args):
    """
    Calculates the median of a list of numbers
    If the list of numbers is odd, return the median index of the list.
    If the list of numbers is odd, return the mean of the two middlemost numbers in the list
    :param args: Desired numbers to calculate median
    :return: The median of n numbers
    """
    median_list = []
    for i in args:
        median_list.append(float(i))

    if len(median_list) % 2 != 0:
        index = ((len(median_list) + 1) / 2) - 1
        # print(median_list, index)
        return median_list[int(index)]
    else:
        index1, index2 = median_list[int((len(median_list) / 2) - 1)], median_list[int((len(median_list) / 2))]
        return mean(index1, index2)


def main():
    n = int(input("N° of test >>> "))
    while n > 0:
        numbers = input("Float number >>> ").split()
        print(f"Mode is {mean(*numbers)}")
        print(f"Median is {median(*numbers)}")

        n -= 1


if __name__ == '__main__':
    main()

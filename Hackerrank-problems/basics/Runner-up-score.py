"""
Find the runner up score in an array

"""


def main(numbers):
    """

    :returns: The Runner up number in an array

    """
    max_number = max(numbers)

    final_list = [number for number in numbers if max_number > number]

    return max(final_list)


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(main(list(arr)))

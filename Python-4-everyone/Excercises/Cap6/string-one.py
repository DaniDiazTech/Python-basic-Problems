"""
File: string-one.py
Author: Daniel Diaz
Github: https://github.com/Daniel1404
Description: Program that recieves a string  and prints the characters
of the string backwards
"""


def reverse(string):
    return string[::-1]


def main():
    """

    :returns: The strings backwards

    """
    string = input("String: ").replace(" ", "_")

    new_string = reverse(string)
    for char in new_string:
        print(char)


if __name__ == "__main__":
    main()

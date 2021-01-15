"""
Given an arbitrary list, write a program that will find and print the last elemental in that list.

Example: If the list is [a, b, c, d], your program should output 'd'.
"""

if __name__ == "__main__":
    my_list = input("Spaced elements: ").split()
    print(my_list[-1])


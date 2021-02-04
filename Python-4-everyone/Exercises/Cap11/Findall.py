"""
Simple program that extracts a Regular expression from a file
"""

import re

def open_file(filename):
    try:
        my_file = open(filename, "r")
        return my_file
    except FileNotFoundError as f:
        print(f)
        exit()


def main():

    filename = input('File name: ')
    read_file = open_file(f"../text/{filename}")

    pattern = "New Revision: ([0-9.]+)"

    avg = []
    for line in read_file:
        regex = re.findall(pattern, line)
        if len(regex) > 0:
            for n in regex:
                avg.append(int(n))

    print(sum(avg) // len(avg))

if __name__ == "__main__":
    main()

"""
Simple program that acts like the grep Unix Program
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
    
    regex = input("Regular expression: ")

    matches = []

    for line in read_file:
        x = re.findall(regex, line)
        if len(x) > 0:
            matches.append(x)
        
    print(f"{filename} had {len(matches)} lines that matched '{regex}'")


if __name__ == "__main__":
    main()

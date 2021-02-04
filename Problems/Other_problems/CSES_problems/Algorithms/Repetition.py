"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
"""


def main():
    string = input()
    counter = 0
    counters = []
    current_character = ""
    for index, character in enumerate(string):
        if character == current_character:
            counter += 1
            if index + 1 == len(string):
                counters.append(counter)
        else:
            counters.append(counter)
            counter = 0
            current_character = character

    print(max(counters) + 1)

if __name__ == "__main__":
    main()


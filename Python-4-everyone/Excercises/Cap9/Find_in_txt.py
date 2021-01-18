"""
Program that finds a word in a text file amazingly fast
thanks to the dictionary IN operator
"""
import string as s

def open_file(filename):
    try:
        my_file = open(filename, "r")
        return my_file
    except FileNotFoundError as f:
        print(f)
        exit()


def find_in_dict(string, dictionary):
    """
    Returns True if the key is in the dictionary, False if not
    """
    if string in dictionary:
        return True
    return False


def main():

    read_file = open_file("../Cap8/romeo-full.txt")
    word_to_search = input("word to search: ").lower()
    word_to_search = word_to_search.translate(word_to_search.maketrans("", "", s.punctuation))

    file_dict = {}

    for line in read_file:
        line = line.translate(line.maketrans("", "", s.punctuation)).lower()
        for word in line.split():
            file_dict[word] = file_dict.get(word, 0) + 1


    print(*[f"The word '{word_to_search}' is in the file" if find_in_dict(
        word_to_search, file_dict) else f"{word_to_search} is not in the file"])

    print(file_dict)

if __name__ == "__main__":
    main()
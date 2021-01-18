"""
Program that finds the date and make a dict and with the days and  teh count
"""
import string as s

def open_file(filename):
    try:
        my_file = open(filename, "r")
        return my_file
    except FileNotFoundError as f:
        print(f)
        exit()


# def find_in_dict(string, dictionary):
#     """
#     Returns True if the key is in the dictionary, False if not
#     """
#     if string in dictionary:
#         return True
#     return False


def main():

    read_file = open_file(f"../text/{input('File name: ')}")
    # word_to_search = input("word to search: ").lower()
    # word_to_search = word_to_search.translate(word_to_search.maketrans("", "", s.punctuation))

    file_dict = {}

    for line in read_file:
        if line.startswith("From") and len(line.split()) > 4:
            # print(line.split())
            file_dict[line.split()[2]] = file_dict.get(line.split()[2], 0) + 1

    print(file_dict)



if __name__ == "__main__":
    main()
"""
Python program to read lines in file1.txt and file2.txt,and merge 
the common words in those two files and
add it to file3.txt
"""

def open_file(filename):

    try:
        myfile = open(filename)

    except FileNotFoundError:
        print("Sorry your file doesn't exist")
        exit()

    return myfile


def read_files(filename):
    """
    Returns the words of a file as a dictionary
    """

    myfile = open_file(filename)

    file_dict = {}

    for line in myfile:

        for word in line.strip():
            file_dict[word] = file_dict.get(word, )





    
    
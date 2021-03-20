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

    file_set = set()

    for line in myfile:

        for word in line.strip():
            file_set.add(word)
    
    return file_set

print(read_files("text_files/romeo.txt"))





    
    
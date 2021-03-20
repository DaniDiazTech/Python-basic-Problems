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


def get_words(filename):
    """
    Returns the words of a file as a dictionary
    """

    myfile = open_file(filename)

    file_set = set()

    for line in myfile:
        
        # just add lowercase words to the set
        for word in line.split():
            file_set.add(word.lower())
    
    return file_set

def merge(read_file1, read_file2, merge_filename):

    words1 = get_words(read_file1)

    words2 = get_words(read_file2)

    common_words = words1.intersection(words2)

    with open(merge_filename, "w") as merge_file:
        
        for word in common_words:
            
            word = word + ", "

            merge_file.write(word)

def main():
    
    mbox = "text_files/mbox.txt"

    romeo = "text_files/romeo.txt"

    merge_file = "merged_files/merge.txt"

    merge(mbox, romeo, merge_file)


if __name__ == "__main__":
    main()









    
    
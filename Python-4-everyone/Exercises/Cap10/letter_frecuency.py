"""
Exercise 3: Write a program that reads a file and prints the letters 
in decreasing order of frequency. Your program should convert all 
the input to lower case and only count the letters a-z. 

Your program should not count spaces, digits, punctuation, or anything other 
than the letters a-z. Find text samples from several different languages and 
see how letter frequency varies between languages. 
Compare your results with the tables at 
https://wikipedia.org/wiki/Letter_frequencies.
"""
import string

def open_file(filename):
    try:
        my_file = open(filename, "r")
        return my_file
    except FileNotFoundError as f:
        print(f)
        exit()


def main():

    read_file = open_file(f"../text/{input('File name: ')}").read().lower()

    file_dict = {}
    
    for character in read_file:
        if character in string.ascii_lowercase:
            file_dict[character] = file_dict.get(character, 0) + 1

    for letter, counter in sorted(file_dict.items(), key = lambda k:k[0]):
        print("Letter:", letter, "Counter:", counter)
    
    print("Most Frequent letter:", *max(file_dict.items(), key= lambda k:k[1]))
    print("Less Frequent letter:", *min(file_dict.items(), key= lambda k:k[1]))

if __name__ == "__main__":
    main()

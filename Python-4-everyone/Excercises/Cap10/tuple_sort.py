"""
Exercise 1: Revise a previous program as follows: 
Read and parse the “From” lines and pull out the addresses 
from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with
 the most commits by creating a list of (count, email) tuples 
 from the dictionary. 
 
 Then sort the list in reverse order and print out the person who has the most commits.
"""
def open_file(filename):
    try:
        my_file = open(filename, "r")
        return my_file
    except FileNotFoundError as f:
        print(f)
        exit()


def main():

    read_file = open_file(f"../text/{input('File name: ')}")

    file_dict = {}

    for line in read_file:
        if line.startswith("From") and len(line.split()) > 2:
            email = line.split()[1]
            file_dict[email] = file_dict.get(email, 0) + 1
    
    sorted_dict = []
    for key, val in file_dict.items():
        sorted_dict.append((val, key))
    
    sorted_dict.sort(reverse=True)

    print("Email with most commits: ", sorted_dict[0][1], sorted_dict[0][0])

if __name__ == "__main__":
    main()

"""
Program that finds an email and counts how much appear in the file
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

    print(file_dict)



if __name__ == "__main__":
    main()
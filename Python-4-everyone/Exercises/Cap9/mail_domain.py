"""
Program that finds an email and counts how much appear
in the file, and prints the email that appears the most
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
            domain = ""
            for i in enumerate(email):
                if i[1] == "@":
                    domain = email[i[0] + 1:]
                    break
            
            file_dict[domain] = file_dict.get(domain, 0) + 1

    print(file_dict)



if __name__ == "__main__":
    main()
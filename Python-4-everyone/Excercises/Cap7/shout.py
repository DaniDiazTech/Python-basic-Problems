def main(filename):
    try:
        read_file = open(filename)
        for line in read_file:
            print(line.upper())

    except FileNotFoundError:
        print("The file doesn't exist in the current directory")
        exit()
        return "Not found"


if __name__ == "__main__":
    main("mbox-short.txt")

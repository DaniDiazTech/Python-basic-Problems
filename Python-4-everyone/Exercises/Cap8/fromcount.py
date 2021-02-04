def main(filename):
    try:
        my_file = open(filename)

    except FileNotFoundError:
        print("No such file in the current directory")
        exit()

    final_line = []

    counter = 0
    for line in my_file:
        words = line.split()

        if len(words) == 0:
            continue
        if words[0] != "From":
            continue
        final_line.append(words[1])
        counter += 1

    return final_line, counter


if __name__ == "__main__":

    filename = input("File name: ")
    lines, count = main(filename)
    for line in lines:
        print(line)

    print(f"There were {count} lines in  the file with From as the first word")

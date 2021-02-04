
def main(filename):
    try:
        my_file = open(filename)

    except FileNotFoundError:
        print("No such file in the current directory")
        exit()

    final_words = []

    for line in my_file:
        words = line.split()
        for word in words:
            if word not in final_words:
                final_words.append(word)

    final_words.sort()
    return final_words


if __name__ == "__main__":

    filename = input("File name: ")
    print("Words: ", main(filename))

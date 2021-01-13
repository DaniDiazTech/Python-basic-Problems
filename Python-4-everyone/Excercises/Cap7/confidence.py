INTERESTING_STRING = "X-DSPAM-Confidence: "


def main(filename):
    try:
        my_file = open(filename)

    except FileNotFoundError:
        print("No such file in the current directory")
        exit()

    average = []

    for line in my_file:
        if not line.startswith(INTERESTING_STRING):
            continue
        decimal_number = float(line.split()[1])
        average.append(decimal_number)

    return sum(average) / len(average)


if __name__ == "__main__":

    filename = input("File name: ")
    print("Average spam confidence: ", main(filename))

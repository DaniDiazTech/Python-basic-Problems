"""
Exercise 2: This program counts the distribution of the hour of the day for
each of the messages. You can pull the hour from the “From” line by 
finding the time string and then splitting that string into parts using the colon 
character. Once you have accumulated the counts for each hour, print out the counts,
one per line, sorted by hour as shown below.
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
        if line.startswith("From") and len(line.split()) > 6:
            hours = line.split()[5]
            hour = hours.split(":")[0]
            file_dict[hour] = file_dict.get(hour, 0) + 1


    hours_dict = sorted(file_dict.items())

    for key, val in hours_dict:
        print("Hour:", key, "Counter:", val)

if __name__ == "__main__":
    main()

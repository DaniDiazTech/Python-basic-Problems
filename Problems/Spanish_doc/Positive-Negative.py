# Read integers and print "-" if they are negative and "+" if they are positive, until  input == 0

def check(number):
    if number > 0:
        return "+"
    elif number < 0:
        return "-"


def main():
    while 1:
        x = int(input("Number >> "))
        if x == 0:
            print("Program finished")
            break
        print(check(x))


if __name__ == '__main__':
    main()

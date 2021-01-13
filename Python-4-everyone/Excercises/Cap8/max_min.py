if __name__ == "__main__":
    numbers = []
    while 1:
        n = input("Enter a number: ")

        if n == "done":
            break
        try:
            numbers.append(float(n))
        except ValueError:
            print("Must be a number")
            continue

    print(f"Maximum: {max(numbers)}\nMinimum: {min(numbers)}")

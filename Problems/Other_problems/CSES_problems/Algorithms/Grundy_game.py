def main():
    test = int(input())
    numbers = [int(input()) for _ in range(test)]
    for n in numbers:
        if n % 2 == 0:
            print("first")
        else:
            print("second")

if __name__ == "__main__":
    main()

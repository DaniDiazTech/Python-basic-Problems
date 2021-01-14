if __name__ == "__main__":
    while 1:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Must be an integer")
            continue
    
    for i in range(1, number + 1):
        
        if i % 3 == 0:
            if i % 5 == 0:
                print("Bang!")
                continue
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
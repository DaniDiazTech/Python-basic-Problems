"""
Given an arbitrary list, find and 
print any elements that are consecutively 
duplicated. 

For example: given the list [a, b, b, a, c, d, d] 
your program should output: "b d".
"""

def get_duplicated(list1):
    duplicated = []
    for index, element in enumerate(list1):
        if not index + 1 == len(list1):
            if element == list1[index + 1] and element not in duplicated:
                duplicated.append(element)
    
    return duplicated

def main():
    my_list = input("Spaced elements: ").split()
    consecutive_list = get_duplicated(my_list)

    print(*consecutive_list)

if __name__ == "__main__":
    main()


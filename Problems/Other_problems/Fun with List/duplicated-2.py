"""
Given an arbitrary list, write a program that will find and print 
any duplicated elements. For example: if you have the list [a, b, c, a, b, d] 
your program should output: "a b".
"""

def find_duplicated(list1):
    """
    Returns a list with duplicated items
    """
    duplicated = []
    for element in list1:
        if list1.count(element) >= 2 and element not in duplicated:
            duplicated.append(element)

    return duplicated
            



def main():
    L1 = ["a", "b", "c", "a", "b", "d"]
    
    duplicated_list = find_duplicated(L1)
    print(*duplicated_list)


if __name__ == "__main__":
    main()

"""
Given an arbitrary list, find and print 
the Nth element of that list. For example: 
given the list [a, b, c, d] , if N=2 then your output should be: 'c'.
(NOTE: Remember that in Python list indexes start from 0 and not 1. 
So in this case, 'a' is the 0th element.)
"""

def main():
    my_list = input("A space separated list: ").split()
    n = input("The index: ")
    
    try:
        number = int(n)
    except ValueError:
        print("Must be a number")
        exit()
    
    if not number >= len(my_list):
        print(my_list[int(n)])
    else:
        print(number, "is too large")
        exit()


if __name__ == "__main__":
    main()
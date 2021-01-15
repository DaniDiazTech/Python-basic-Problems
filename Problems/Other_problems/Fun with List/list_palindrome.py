"""
A palindrome is something that can be read 
the same way forwards and backwards. In English, 
the common example is 'racecar,' because no matter 
which way you read it, it still spells the same word. 
Given an arbitrary list, write a program that can determine 
if the list is palindromic, and prints True if it is, 
or False otherwise. 

For example: if given the list [a, b, a] your program should output True.
"""

def palindrome(list1):

    return list1 == list1[::-1]

def main():
    # my_list = ["a", "a", "b", "c", "a", "d", "d", "c", "b"]
    
    my_list = input("Palindrome elements: ").split()
    print(*["The list is palindrome" if  palindrome(my_list) else "List isn't Palindrome"])


if __name__ == "__main__":
    main()

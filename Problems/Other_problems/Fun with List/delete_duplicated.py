"""
For an arbitrarily given list, write a program that will
find and delete any consecutively duplicated elements. 
For example, if given the list [a, a, b, c, a, d, d, c, b] your 
program should output: [a, b, c, a, d, c, b].
"""

def delete_duplicated(list1):
    copy_list = list1.copy()

    remove_index = [] 

    counter = 0
    for index, element in enumerate(list1):
        """
        Check if the current element is the same as the next element
        and remove it
        """
        if not index + 1 == len(list1):
            if element == list1[index + 1]:
                remove_index.append(index)
    
    for i in remove_index:
        del copy_list[i - counter]
        counter += 1
    
    return copy_list

def main():
    # my_list = ["a", "a", "b", "c", "a", "d", "d", "c", "b"]
    
    my_list = input("Spaced elements: ").split()
    print("List without duplicated", delete_duplicated(my_list))


if __name__ == "__main__":
    main()

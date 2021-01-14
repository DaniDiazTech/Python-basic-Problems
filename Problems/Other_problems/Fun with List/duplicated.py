"""
Given two lists, find and print the elements that are 
present in both lists. For example: if given the list 
L1 = [a, b, c, d] and L2 = [a, c, e, f] 
then your program should output: "a c".
"""


def remove_elements(list1, list2):
    """
    Returns a  list with the repeated elements of the two lists
    """
    removed_elements = []

    for element in list1:
        if element in list2:
            removed_elements.append(element)

            # UNCOMMENT THE FOLLOWINF TO ALSO REMOVE THE REPEATED ELEMENTS IN THE LIST
            # list1.remove(element)
            # list2.remove(element)
    
    return removed_elements



def main():
    
    L1 = ["a", "b", "c", "d"]
    L2 = ["a", "c", "e", "f"]

    removed = remove_elements(L1, L2)

    for i in removed:
        print(i)
    
    # print(L1)
    # print(L2)



if __name__ == "__main__":
    main()

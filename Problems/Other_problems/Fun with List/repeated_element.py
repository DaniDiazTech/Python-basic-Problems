"""
To find the positions of the repeated value in a list
"""

def find_repeated_element(special_list):

    repeated_elements = []

    # Iterates over one index of the special list
    for i in range(len(special_list)):

        # Iterates from the next element of the list, up to the end
        for j in range(i + 1, len(special_list)):

            # compares each element and appends it's index
            if  special_list[i] == special_list[j]:
                repeated_elements.append((i, j))

    return repeated_elements

def main():

    my_list = input("A list >> ").split()

    repeated = find_repeated_element(my_list)


    print("The indexes of the repeated elements are: ", end="")

    print(*[index for index in repeated])


if __name__ == "__main__":
    main()
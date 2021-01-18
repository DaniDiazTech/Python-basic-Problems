"""
Triangle program
Read an integer that indicates the number of input to read.
Then return a triangle with the lenght of the input.


in    out
3

5
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
3
    *
    **
    ***
    **
    *
2
    *
    **
    *
"""


class Triangle:

    """Class that returns a triangle. """

    def __init__(self, lenght):
        self.lenght = lenght

    def get_triangle(self):
        triangle = ""
        down_triangle = ""
        for i in range(self.lenght + 1):
            triangle += "*" * i
            triangle += "\n"

        for i in range(self.lenght - 1, 0, -1):
            down_triangle += "*" * i
            down_triangle += "\n"

        return triangle + down_triangle


def main():
    try:
        n = int(input("Number of Triangles > "))
        while n > 0:
            triangle_lenght = int(input("Lenght of the Triangle > "))
            my_triangle = Triangle(triangle_lenght)
            print(my_triangle.get_triangle())
            n -= 1
    except ValueError as e:
        print(f"Error : {e}")
        print("You must enter a number!")
        main()


if __name__ == "__main__":
    main()

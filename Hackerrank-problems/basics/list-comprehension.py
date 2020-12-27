"""
Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1],
[1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0],
[2, 2, 1], [2, 2, 2]]

"""


def main():
    x, y, z, n = (int(input("A number :) ")) for _ in range(4))

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1)
           for k in range(z + 1) if sum([i, j, k]) != n])


if __name__ == '__main__':
    main()

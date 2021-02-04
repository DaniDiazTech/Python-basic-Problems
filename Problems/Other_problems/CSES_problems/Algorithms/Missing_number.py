"""
Time limit: 1.00 s Memory limit: 512 MB
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
2≤n≤2⋅105
Example

Input:
5
2 3 1 5

Output:
4
"""


def main():
    total_numbers = int(input())
    numbers = [int(i) for i in input().split()]

    total = total_numbers * (total_numbers + 1) / 2
    print(int(total - sum(numbers)))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# import math
import os
# import random
# import re
# import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    new_list = []
    number_of_pairs = 0
    for sock in ar:
        if sock in new_list:
            new_list.remove(sock)
            number_of_pairs += 1
        else:
            new_list.append(sock)

    return number_of_pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
    
    # fptr.write(str(result) + '\n')

    # fptr.close()

#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == "U":

            # We do an up step here
            level += 1

        else:
            # We do a down step here
            level -= 1

        if level == 0 and step == "U":
            # We come from sea level
            valleys += 1

    return valleys


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c) - 1
    print('length: ', n)
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return 1 + min(jumpingOnClouds(c[(n - 1):]), jumpingOnClouds(c[(n - 2):]))

def min_jump_required(c, n):
    if n == 0:
        return
    if n == 1 or n == 2:
        return 1
    else:
        return 1 + min(min_jump_required(c, n - 1), min_jump_required(c, n - 2))

if __name__ == '__main__':

    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    print(c[:3])
    print(c[3:])

    result = jumpingOnClouds(c)
    print(result)

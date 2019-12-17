"""
判断一个数是不是素数
"""

import math


def is_primer(num):
    turn = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            turn = False
            break
    return turn


"""
实现计算求最大公约数和最小公倍数的函数
"""
import math


def factor(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            print("{}是{}和{}最大公约数".format(i, a, b))
            print("{}是{}和{}最大公约数".format(a * b // i, a, b))
            break

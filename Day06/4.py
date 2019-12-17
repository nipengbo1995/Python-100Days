"""
写一个程序判断输入的正整数是不是回文素数
"""


import math


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_primer(num):
    turn = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            turn = False
            break
    return turn


if __name__ == '__main__':
    test_num = int(input('请输入正整数: '))
    if is_palindrome(test_num) and is_primer(test_num):
        print("{}是回文素数".format(test_num))

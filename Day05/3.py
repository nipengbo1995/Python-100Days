"""
输出100以内所有素数
提示：素数只能被1和本身整除
"""
import math
for i in range(2, 100):
    turn = True
    for j in (2, int(math.sqrt(i)) + 1):
        if i % j == 0 and j != 1 and j != i:
            turn = False
            break
    if turn:
        print(i)

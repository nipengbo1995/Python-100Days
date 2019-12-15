"""
找出10000以内的完美数。

例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）

"""


for i in range(2, 10000):
    sum_factor = 0
    for j in range(1, i):
        if i % j == 0:
            sum_factor += j
    if i == sum_factor:
        print(i)


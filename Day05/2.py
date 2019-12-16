"""
找出10000以内的完美数。

例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）

下面方法运行较慢
for i in range(2, 10000):
    sum_factor = 0
    for j in range(1, i):
        if i % j == 0:
            sum_factor += j
    if i == sum_factor:
        print(i)
"""
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num//factor
    if result == num:
        print(num)





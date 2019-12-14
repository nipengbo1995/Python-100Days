"""
输入两个正整数计算它们的最大公约数和最小公倍数

"""
x = int(input('x= '))
y = int(input('y= '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('{:d}和{:d}的最大公约数是{:d}'.format(x, y, factor))
        print('{:d}和{:d}的最小公倍数是{:d}'.format(x, y, x * y // factor))
        break

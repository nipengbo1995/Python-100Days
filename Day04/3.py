"""
打印三角形图案

"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(2 * row):
        if row - i - 1 < _ < row + i + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

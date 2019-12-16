import math
for i in range(2, 100):
    for j in (1, int(math.sqrt(i)) + 1):
        if i % j == 0 and j != 1 and j != i:
            print("{}不是素数".format(i))
            break
        else:
            print("{}是素数".format(i))

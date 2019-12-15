filename = '安全试验.txt'

with open(filename, encoding="utf-8") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip('！\n'))

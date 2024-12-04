from sys import argv

n, m = map(int, argv[1:3])

circular_array = list(range(1, n + 1))

way = []
index = 0

while True:
    way.append(circular_array[index])
    index = (index + m - 1) % n
    if index == 0:
        break

print(''.join(map(str, way)))
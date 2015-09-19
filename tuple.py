__author__ = 'tienvm'

x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]

x1 = list(set(x))
y1 = list(set(y))
listTuple = []
for i in x1:
    for j in y1:
        if i + j < 10:
            listTuple.append((i, j))
print(list(listTuple))

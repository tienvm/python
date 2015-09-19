__author__ = 'tienvm'

x = [1, 5, 7, 3, 8]

ListXEnumerates = list(enumerate(x))
for a, b in ListXEnumerates:
    print('X[{0}] = {1}'.format(a, b))


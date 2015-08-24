__author__ = 'tienvm'
print('---', end='')
for a in range(1, 10):
    print('%4d' % a, end='')
print('\n')
a = 0
for i in range(1, 10):
    a += 1
    print('%1d ||' % a, end='')
    for j in range(1, 10):
        print('%3d ' % (i * j), end='')

    print('\n', end='')
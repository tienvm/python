__author__ = 'tienvm'


def convert(n):
    str = '1'
    for i in range(1, n):
        str += '0'
    return int(str)

a = 534534
arr = ['Khong', 'Mot', 'Hai', 'Ba', 'Bon', 'Nam', 'Sau', 'Bay', 'Tam', 'Chin']

if isinstance(a, int):
    for i in reversed(range(0, len(str(a)) + 1)):
        if i == 0:
            print('')
        else:
            print('%1s ' % arr[int(a/convert(i))], end='')

        if i % 9 == 1 and int(i / 9):
            print(' Ty " ', end='')
        elif i % 3 == 1 and int(i / 3) > 0 and i % 6 != 1:
            print(' Nghin " ', end='')
        elif i % 6 == 1 and int(i / 6):
            print(' Trieu " ', end='')
        if i % 3 == 0 and i > 2:
            print(' Tram . ', end='')

        a %= convert(i)
else:
    print('Khong phai INT')





__author__ = 'tienvm'

listArr = ['a', 'b', 'a', 'd', 'b', 'a', 'e']


def unique(lists: []):
    count = 0
    arr = []
    for a in range(0, len(lists)):
        for b in range(0, len(lists)):
            if lists[a] is lists[b]:
                count += 1
        if count == 1:
            arr.append(lists[a])
        count = 0
    return arr


print(list(unique(listArr)))

__author__ = 'tienvm'

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']


def exercise1(arr1: [], arr2: []):
    if len(arr1) != len(arr2):
        return 'Error'
    tuples = []
    for s1 in range(0, len(arr1)):
        for s2 in reversed(range(0, len(arr2))):
            if s1 + s2 == len(arr1) - 1:
                tuples.append((arr1[s1], arr2[s2]))
    return tuples

print(list(exercise1(l1, l2)))


numList = [1, 3, 5, 7, 9, 0, 11]


def numListSort(arr: []):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tg = arr[i]
                arr[i] = arr[j]
                arr[j] = tg
    return arr


def exercise2(arr: []):
    arrSort = numListSort(arr)
    tuples = []
    arr1 = []
    arr2 = []
    for list in arrSort:
        if list <= 5:
            arr1.append(list)
        else:
            arr2.append(list)
    tuples.append((arr1, arr2))
    return tuples
print(list(exercise2(numList)))

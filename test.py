import random
strings = 'awertyhgjkbmlciogxwq'
arr = []

for i in range(0, 10):
    keyRandom = random.randrange(len(strings))
    arr.append(strings[keyRandom])

print('Du lieu mau : {0}'.format(arr))
print('Mang sau khi sap xep la :')

for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            tg = arr[i]
            arr[i] = arr[j]
            arr[j] = tg

print(arr)
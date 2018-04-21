# Uses python3
import numpy as np

def naive(n, a):
    # n = int(input())
    # a = [int(x) for x in input().split()]
    assert(len(a) == n)

    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    print(result)

def fast1(n, a):
    # n = int(input())
    # a = [int(x) for x in input().split()]
    assert(len(a) == n)

    index1 = 0
    index2 = 0

    for i in range(0, n):
        if a[i] > a[index1]:
            index1 = i
            break

    if index1 == 0:
      index2 = 1

    for i in range(0, n):
        if a[i] > a[index2] and i != index1:
            index2 = i
            break

    result = a[index1] * a[index2]
    print(result)

def fast2(n, a):
    # n = 10
    # a = [68165, 87637, 74297, 2904, 32873, 86010, 87637, 66131, 82858, 82935]
    # n = int(input())
    # a = [int(x) for x in input().split()]
    assert(len(a) == n)

    index = 0

    for i in range(0, n - 1):
        if a[i] > a[index]:
            index = i
            break

    temp = a[n-1]
    a[n-1] = a[index]
    a[index] = temp
    index = 0

    for i in range(0, n - 2):
        if a[i] > a[index]:
            index = i
            break
    result = a[n-1] * a[index]
    print(result)


## Stress testing

while True:

   n = np.random.randint(2, 1000, 1, dtype="int64")[0]
   print(n)

   a = []

   for _ in range(0, n):
       a.append(np.random.randint(0, 99999, 1, dtype="int64")[0])

   for i in range(0, n):
       print(a[i], end=' ')

   res1 = naive(n, a)
   res2 = fast(n, a)

   if res1 != res2:
       print('\n Womp. {} and {}\n'.format(res1, res2))
       break
   else:
       print('\nWoot\n')

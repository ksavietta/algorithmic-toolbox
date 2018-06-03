# Uses python3
import sys

def binary_search(array, key):
    low, high = 0, len(array) - 1
    return bsearch(array, low, high, key)

def bsearch(array, low, high, key):
    if high < low:
        return -1
    midIndex = low + ((high - low) // 2)
    if array[midIndex] == key:
        return midIndex
    if key > array[midIndex]:
        return bsearch(array, midIndex + 1, high, key)
    else:
        return bsearch(array, low, midIndex - 1, key)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

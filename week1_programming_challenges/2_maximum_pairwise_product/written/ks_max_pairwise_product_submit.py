# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

index = 0

for i in range(0, n):
    if a[i] > a[index]:
        index = i

temp = a[n-1]
a[n-1] = a[index]
a[index] = temp
index = 0

for i in range(0, n - 1):
    if a[i] > a[index]:
        index = i

result = a[n-1] * a[index]
print(result)

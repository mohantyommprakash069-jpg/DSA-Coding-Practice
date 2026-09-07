a = [1, 2, 3, 7, 0, 0, 0, 0, 0]
b = [5, 6, 8, 9, 10]

i = 3
j = len(b) - 1
k = len(a) - 1

while i >= 0 and j >= 0:
    if a[i] > b[j]:
        a[k] = a[i]
        i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1
while j >= 0:
    a[k] = b[j]
    j -= 1
    k -= 1

print(a)
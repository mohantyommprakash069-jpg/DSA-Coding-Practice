arr = [10, 20, 30, 40, 50]

pos = 2
val = 90

arr.append(0)

ub = len(arr) - 1

for i in range(ub, pos, -1):
    arr[i] = arr[i - 1]

arr[pos] = val

ub += 1

print(arr)
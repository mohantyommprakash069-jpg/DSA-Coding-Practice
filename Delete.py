arr = [10, 20, 30, 40, 50, 60]
lb = 0
ub = len(arr) - 1
pos = 2
for i in range(pos, ub):
    arr[i] = arr[i + 1]
arr.pop()
ub -= 1
print(arr)
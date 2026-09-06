arr = [10, 20, 30, 40, 50]
key=30
found=False
for i in range(len(arr)):
    if arr[i]==key:
        Found=True
        print(f"index={i}")
        break
if not found:
    print("not found")
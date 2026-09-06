arr=[10,20,30,40,50,60]
lb=0
ub=len(arr)-1
key=20

while lb<=ub:
    mid=(lb+ub)//2
    if arr[mid]==key:
        print("fouind element at",mid)
    if key>arr[mid]:
        lb=mid+1
    if key<arr[mid]:
        ub=mid-1
print("element not found")

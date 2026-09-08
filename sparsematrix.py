a=[[0,0,0,0,0],[0,10,0,0,0],[0,0,0,0,20],[30,0,0,0,0],[0,0,40,50,0],[0,60,0,0,0]]
print(a)
m = len(a)
n = len(a[0])
nz=0
for i in range(5):
    for j in range(5):
        if a[i][j]!=0:
            nz+=1

if (nz>=(m*n)/2):
    print("it is not sparse matrix")
else:
    print("it is a sparse")
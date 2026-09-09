size=int(input("enter size of stack -->"))

stack=[0]*size
top=-1
n=int(input("enter number of element in stack"))
for i in range(n):
    value=int(input("enter value"))

    if top == size-1:
        print("Stack Overflow")
        break
    else:
        top+=1
        stack[top]=value
print("stack:",stack[:top+1])
    

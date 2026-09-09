stack = [1, 2, 3]
top = 2

if top == -1:
    print("Stack Underflow")
else:
    print("Popped:", stack[top])
    top -= 1

print("Stack:", stack[:top + 1])
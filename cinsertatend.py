class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

start = None
temp = None

value = [10, 20, 30, 40]

for i in value:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh

temp.next = start

fresh = Node(25)

if start is None:
    start = fresh
    temp = fresh
    temp.next = start
else:
    temp = start

    while temp.next is not start:
        temp = temp.next

    temp.next = fresh
    fresh.next = start

temp = start

while True:
    print(temp.data, end=" -> ")
    temp = temp.next

    if temp == start:
        break

print("back to start")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None

values = [10, 20, 30, 40]

for i in values:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh

temp.next = start

temp = start

while True:
    print(temp.data, end=" -> ")
    temp = temp.next

    if temp == start:
        break

print("back to start")
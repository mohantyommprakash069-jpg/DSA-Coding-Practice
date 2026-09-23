class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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
        fresh.prev = temp
        temp = fresh


pos = 3

temp = start
i = 1

while i < pos:
    temp = temp.next
    i += 1

temp.prev.next = temp.next

if temp.next is not None:
    temp.next.prev = temp.prev


temp = start

while temp is not None:
    print(temp.data, end=" <-> ")
    temp = temp.next
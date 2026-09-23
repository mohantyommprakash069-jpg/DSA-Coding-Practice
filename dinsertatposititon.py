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
fresh = Node(25)

temp = start
i = 1

while i < pos - 1:
    temp = temp.next
    i += 1

fresh.next = temp.next
fresh.prev = temp
temp.next.prev = fresh
temp.next = fresh


temp = start

while temp is not None:
    print(temp.data, end=" <-> ")
    temp = temp.next
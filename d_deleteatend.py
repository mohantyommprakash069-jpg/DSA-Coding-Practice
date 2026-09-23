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


temp = start

while temp.next is not None:
    temp = temp.next

temp.prev.next = None


temp = start

while temp is not None:
    print(temp.data, end=" <-> ")
    temp = temp.next
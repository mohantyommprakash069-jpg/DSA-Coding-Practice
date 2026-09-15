class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None

values = [10, 20, 30]

for i in values:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh


pos = 2

if start is None:
    print("linked list does not exist")

elif pos == 1:
    start = start.next

else:
    temp = start
    i = 1

    while temp is not None and i < pos - 1:
        temp = temp.next
        i += 1

    if temp is not None and temp.next is not None:
        temp.next = temp.next.next


temp = start

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
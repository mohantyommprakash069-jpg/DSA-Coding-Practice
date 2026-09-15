class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None

values = [10, 20, 30]

# Create linked list
for i in values:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh


# Insert 35 at specific position
fresh = Node(35)
pos = 3

if pos == 1:
    fresh.next = start
    start = fresh

else:
    temp = start
    i = 1

    while temp is not None and i < pos - 1:
        temp = temp.next
        i += 1

    if temp is not None:
        fresh.next = temp.next
        temp.next = fresh


# Display
temp = start

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
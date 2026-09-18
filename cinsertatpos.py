class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None

value = [10, 20, 30, 40]

# Create circular linked list
for i in value:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh

temp.next = start


# Insert 25 at position 2
fresh = Node(25)
pos = 2

if start is None:
    start = fresh
    fresh.next = start

elif pos == 1:
    temp = start

    while temp.next != start:
        temp = temp.next

    fresh.next = start
    temp.next = fresh
    start = fresh

else:
    temp = start
    i = 1

    while i < pos - 1:
        temp = temp.next
        i += 1

    fresh.next = temp.next
    temp.next = fresh


# Display circular linked list
temp = start

while True:
    print(temp.data, end=" -> ")
    temp = temp.next

    if temp == start:
        break

print(" back to start")
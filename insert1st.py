class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None

values = []

# Create linked list
for i in values:
    fresh = Node(i)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh


# Insert 35 at first
fresh = Node(35)

if start is None:
    start = fresh
else:
    fresh.next = start
    start = fresh


# Display
temp = start

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


temp = None
start = None

value = [10, 20, 30, 40]

# Create circular linked list
for i in value:
    fresh = Node(i)

    if start == None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh

temp.next = start


# DELETE AT END
if start == None:
    print("Circular Linked List does not exist")

elif start.next == start:
    # Only one node
    start = None

else:
    temp = start

    # Find second-last node
    while temp.next.next != start:
        temp = temp.next

    # Delete last node
    temp.next = start


# Display
if start == None:
    print("List is empty")
else:
    temp = start

    while True:
        print(temp.data, end=" -> ")
        temp = temp.next

        if temp == start:
            break

    print("back to start")
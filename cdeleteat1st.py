class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
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


if start.next == start:
    start=None
else:
    temp=start

    while temp.next != start:
        temp=temp.next
    
    start = start.next
    temp.next=start

temp = start

while True:
    print(temp.data, end=" -> ")
    temp = temp.next

    if temp == start:
        break

print("back to start")

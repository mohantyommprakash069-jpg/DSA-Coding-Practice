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



if start is None:
    print("linked list does not exist")
else:
    temp=start
    while temp.next is not None:
        prev=temp
        temp=temp.next
    prev.next=None


# Display
temp = start

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
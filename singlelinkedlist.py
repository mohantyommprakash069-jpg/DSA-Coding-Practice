class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


start = None
temp = None



# Create linked list
for i in range(3):
    values = int(input("enter one node value"))
    fresh = Node(values)

    if start is None:
        start = fresh
        temp = fresh
    else:
        temp.next = fresh
        temp = fresh

temp = start

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
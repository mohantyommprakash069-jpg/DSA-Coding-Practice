# Queue using Array

size = 5
q = [0] * size

front = -1
rear = -1

# Insertion
print("=== Queue Insertion ===")

for i in range(size):

    item = int(input("Enter value for inserting: "))

    if rear == size - 1:
        print("Queue is Overflow")

    elif front == -1 and rear == -1:
        front = rear = 0
        q[rear] = item

    else:
        rear += 1
        q[rear] = item

print("\nQueue after insertion:", q)


# Deletion
print("\n=== Queue Deletion ===")

for i in range(size):

    if front == -1 and rear == -1:
        print("Queue is Empty")

    elif front == rear:
        print("Deleted element is =", q[front])
        front = rear = -1

    else:
        print("Deleted element is =", q[front])
        front += 1

print("\nQueue after deletion:", q)
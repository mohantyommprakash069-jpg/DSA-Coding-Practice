# Circular Queue using Array

size = 5
q = [0] * size

front = -1
rear = -1

# ---------------- INSERTION ----------------

print("=== Circular Queue Insertion ===")

for i in range(size):

    item = int(input("Enter value for inserting: "))

    # Queue is full
    if (rear + 1) % size == front:
        print("Circular Queue is Overflow")

    # Queue is empty
    elif front == -1 and rear == -1:
        front = rear = 0
        q[rear] = item

    # Normal / Circular insertion
    else:
        rear = (rear + 1) % size
        q[rear] = item

print("\nQueue after insertion:", q)


# ---------------- DELETION ----------------

print("\n=== Circular Queue Deletion ===")

for i in range(size):

    if front == -1 and rear == -1:
        print("Circular Queue is Empty")

    # Only one element
    elif front == rear:
        print("Deleted element is =", q[front])
        front = rear = -1

    # Normal / Circular deletion
    else:
        print("Deleted element is =", q[front])
        front = (front + 1) % size
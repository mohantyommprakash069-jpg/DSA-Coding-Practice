# T4LinkedListPython
# Singly Linked List - Menu Driven Program
# Operations:
# 1. Insert at Head
# 2. Insert at Tail
# 3. Insert at Position
# 4. Delete Head
# 5. Delete Tail
# 6. Delete Node
# 7. Search
# 8. Length
# 9. Display
# 10. Exit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at Tail
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # 3. Insert at Position
    # Position starts from 1
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_at_head(data)
            return

        current = self.head
        count = 1

        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 4. Delete Head
    def delete_head(self):
        if self.head is None:
            print("List is empty.")
            return

        deleted_value = self.head.data
        self.head = self.head.next
        print(f"Deleted: {deleted_value}")

    # 5. Delete Tail
    def delete_tail(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            print(f"Deleted: {deleted_value}")
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data
        current.next = None
        print(f"Deleted: {deleted_value}")

    # 6. Delete Node
    # Deletes the first occurrence of the given value
    def delete_node(self, data):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == data:
            self.delete_head()
            return

        current = self.head

        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is None:
            print("Node not found.")
            return

        current.next = current.next.next
        print(f"Deleted: {data}")

    # 7. Search
    # Returns position if found, otherwise -1
    def search(self, data):
        current = self.head
        position = 1

        while current is not None:
            if current.data == data:
                return position

            current = current.next
            position += 1

        return -1

    # 8. Length
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def main():
    llOne = LinkedList()
    choice = 0

    while choice != 10:
        print("\n========== SINGLY LINKED LIST ==========")
        print("1. Insert at Head")
        print("2. Insert at Tail")
        print("3. Insert at Position")
        print("4. Delete Head")
        print("5. Delete Tail")
        print("6. Delete Node")
        print("7. Search")
        print("8. Length")
        print("9. Display")
        print("10. Exit")
        print("========================================")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                data = int(input("Enter data: "))
                llOne.insert_at_head(data)
                print("Node inserted at head.")

            case 2:
                data = int(input("Enter data: "))
                llOne.insert_at_tail(data)
                print("Node inserted at tail.")

            case 3:
                data = int(input("Enter data: "))
                position = int(input("Enter position (starting from 1): "))
                llOne.insert_at_position(data, position)

            case 4:
                llOne.delete_head()

            case 5:
                llOne.delete_tail()

            case 6:
                data = int(input("Enter data to delete: "))
                llOne.delete_node(data)

            case 7:
                data = int(input("Enter data to search: "))
                position = llOne.search(data)

                if position == -1:
                    print("Node not found.")
                else:
                    print(f"Node found at position {position}.")

            case 8:
                print(f"Length of linked list: {llOne.length()}")

            case 9:
                llOne.display()

            case 10:
                print("Program ended.")

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

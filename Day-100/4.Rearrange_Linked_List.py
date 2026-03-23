class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(" ".join(map(str, result)))

def user_logic(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    # Create dummy nodes for 3 groups
    first_dummy = Node(0)
    second_dummy = Node(0)
    third_dummy = Node(0)

    first_tail = first_dummy
    second_tail = second_dummy
    third_tail = third_dummy

    current = linked_list.head
    position = 1

    while current:
        next_node = current.next
        current.next = None  # detach node

        if position % 3 == 1:
            first_tail.next = current
            first_tail = current
        elif position % 3 == 2:
            second_tail.next = current
            second_tail = current
        else:
            third_tail.next = current
            third_tail = current

        current = next_node
        position += 1

    # Connect the three groups
    first_tail.next = second_dummy.next
    second_tail.next = third_dummy.next

    # Update head
    linked_list.head = first_dummy.next

    # Update tail
    if third_tail != third_dummy:
        linked_list.tail = third_tail
    elif second_tail != second_dummy:
        linked_list.tail = second_tail
    else:
        linked_list.tail = first_tail

    return linked_list

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer N
    elements = list(map(int, data[1:]))  # Remaining input is the elements of the linked list

    # Initialize the linked list and add elements
    ll = LinkedList()
    for element in elements:
        ll.push(element)

    # Call user logic function
    modified_ll = user_logic(ll)

    # Print the modified linked list
    modified_ll.print_list()

if __name__ == "__main__":
    main()
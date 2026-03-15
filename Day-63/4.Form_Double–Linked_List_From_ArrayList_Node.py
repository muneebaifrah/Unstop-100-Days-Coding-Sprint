class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_linked_list(row):
    head = Node(row[0])
    current = head
    for value in row[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def print_doubly_linked_list(head):
    current = head
    while current:
        print(current.data, end=" <---> " if current.next else " <---> null\n")
        current = current.next

def main():
    # Input handling
    N = int(input())
    M = int(input())

    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # Step 1: Create list of linked lists (ArrayList of Nodes)
    node_list = []
    for row in arr:
        head = create_linked_list(row)
        node_list.append(head)

    # Step 2: Rearranging: even indices first, then odd indices
    order = []
    for i in range(N):
        if i % 2 == 0:
            order.append(node_list[i])
    for i in range(N):
        if i % 2 != 0:
            order.append(node_list[i])

    # Step 3: Merge into a single doubly linked list
    dummy = Node(0)
    tail = dummy

    for head in order:
        current = head
        while current:
            new_node = Node(current.data)
            tail.next = new_node
            new_node.prev = tail
            tail = new_node
            current = current.next

    # Step 4: Print the final linked list
    print_doubly_linked_list(dummy.next)

# Run the program
if __name__ == "__main__":
    main()
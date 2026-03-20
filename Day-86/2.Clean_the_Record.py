class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            current = current.next
    return head

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    print(len(result))
    if result:
        print(*result)

# Read input
N = int(input())
if N == 0:
    print(0)
else:
    values = list(map(int, input().split()))

    # Build linked list
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    # Remove duplicates
    updated_head = remove_duplicates(head)

    # Print result
    print_list(updated_head)
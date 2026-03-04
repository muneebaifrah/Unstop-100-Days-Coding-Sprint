class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def check(l1, l2):
    values = set()

    # Store all values of first list
    while l1:
        values.add(l1.val)
        l1 = l1.next

    # Check if any value appears in second list
    while l2:
        if l2.val in values:
            return 1
        l2 = l2.next

    return 0


# ---------------- DRIVER CODE ---------------- #

def build_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    head1 = build_linked_list(arr1)
    head2 = build_linked_list(arr2)

    print(check(head1, head2))
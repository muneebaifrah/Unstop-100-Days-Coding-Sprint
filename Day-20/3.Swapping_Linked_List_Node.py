class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head, k):
    if not head:
        return head

    first = head

    # Move to kth node from start
    for _ in range(k - 1):
        first = first.next

    kth_from_start = first

    # Find kth node from end
    second = head
    temp = first

    while temp.next:
        temp = temp.next
        second = second.next

    kth_from_end = second

    # Swap values
    kth_from_start.val, kth_from_end.val = (
        kth_from_end.val,
        kth_from_start.val,
    )

    return head


# ---------------- MAIN DRIVER ---------------- #

def build_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" ".join(result))


if __name__ == "__main__":
    N = int(input())
    values = list(map(int, input().split()))
    K = int(input())

    head = build_linked_list(values)
    head = swapNodes(head, K)
    print_linked_list(head)
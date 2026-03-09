class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def build_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n, m = data[0], data[1]
    arr1 = data[2:2+n]
    arr2 = data[2+n:2+n+m]

    l1 = build_list(arr1)
    l2 = build_list(arr2)

    merged = merge_lists(l1, l2)
    print_list(merged)


if __name__ == "__main__":
    main()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def stringToListNode(inp):
    inp = inp.strip()[1:-1]
    if not inp:
        return None

    node_values = list(map(int, inp.split(",")))

    dummy = ListNode(0)
    ptr = dummy

    for v in node_values:
        ptr.next = ListNode(v)
        ptr = ptr.next

    return dummy.next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next


def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    inp = input().strip()
    head = stringToListNode(inp)
    head = swapPairs(head)
    printList(head)
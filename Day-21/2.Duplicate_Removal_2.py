class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_node(head, val):
    new_node = ListNode(val)
    if head[0] is None:
        head[0] = new_node
        return
    
    temp = head[0]
    while temp.next:
        temp = temp.next
    temp.next = new_node


def deleteDuplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        if curr.next and curr.val == curr.next.val:
            dup_val = curr.val
            while curr and curr.val == dup_val:
                curr = curr.next
            prev.next = curr
        else:
            prev = prev.next
            curr = curr.next

    return dummy.next


if __name__ == "__main__":
    n = int(input().strip())
    head = [None]

    for _ in range(n):
        val = int(input().strip())
        insert_node(head, val)

    new_head = deleteDuplicates(head[0])

    if not new_head:
        print("null")
    else:
        temp = new_head
        res = []
        while temp:
            res.append(str(temp.val))
            temp = temp.next
        print(" ".join(res))
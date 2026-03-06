class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def remove_last_occurrences(head):
    arr = []
    temp = head
    
    while temp:
        arr.append(temp.val)
        temp = temp.next
    
    last_pos = {}
    for i, v in enumerate(arr):
        last_pos[v] = i
    
    dummy = ListNode(0)
    curr = dummy
    
    for i, v in enumerate(arr):
        if last_pos[v] != i:
            curr.next = ListNode(v)
            curr = curr.next
    
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" ".join(res))


if __name__ == "__main__":
    n = int(input().strip())
    
    if n == 0:
        exit()
    
    arr = list(map(int, input().split()))
    
    head = build_list(arr)
    
    head = remove_last_occurrences(head)
    
    print_list(head)
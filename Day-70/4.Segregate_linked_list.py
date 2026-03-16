class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def segregate(head, x):
    div_head = div_tail = None
    nondiv_head = nondiv_tail = None
    
    current = head
    while current:
        if current.data % x == 0:
            if not div_head:
                div_head = div_tail = current
            else:
                div_tail.next = current
                div_tail = current
        else:
            if not nondiv_head:
                nondiv_head = nondiv_tail = current
            else:
                nondiv_tail.next = current
                nondiv_tail = current
        current = current.next
    
    # Join the two lists
    if div_tail:
        div_tail.next = nondiv_head
    if nondiv_tail:
        nondiv_tail.next = None
    
    return div_head if div_head else nondiv_head

# Helper to build and print linked list
def build_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    print(" ".join(res))

# Driver
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

head = build_linked_list(arr)
new_head = segregate(head, x)
print_linked_list(new_head)
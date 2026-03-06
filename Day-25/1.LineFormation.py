# Python 3
import sys

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def minChanges(head, n):
    arr = []
    curr = head

    # store linked list values
    while curr:
        arr.append(curr.val)
        curr = curr.next

    # sorted order
    sorted_arr = sorted(arr)

    # count mismatches
    count = 0
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            count += 1

    return count


# -------- input handling --------
n = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().split()))

# build linked list
head = Node(values[0])
curr = head
for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

# output
print(minChanges(head, n))
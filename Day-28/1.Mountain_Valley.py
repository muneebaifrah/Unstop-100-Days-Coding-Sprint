class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def countNodes(head):
    if not head or not head.next:
        return 0

    prev = head
    curr = head.next
    count = 0

    while curr and curr.next:
        if curr.data > prev.data and curr.data > curr.next.data:
            count += 1

        prev = curr
        curr = curr.next

    return count


# ---------- Input Handling ----------
n = int(input().strip())
arr = list(map(int, input().split()))

# Build linked list
head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

print(countNodes(head))
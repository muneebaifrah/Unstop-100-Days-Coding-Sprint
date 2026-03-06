class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(size, elements):
    if size == 0:
        return None
    
    head = Node(elements[0])
    curr = head
    
    for i in range(1, size):
        curr.next = Node(elements[i])
        curr = curr.next
    
    return head


def max_symmetric_sum(head):
    arr = []
    
    # Convert linked list to array
    temp = head
    while temp:
        arr.append(temp.val)
        temp = temp.next
    
    i = 0
    j = len(arr) - 1
    max_sum = float('-inf')
    
    while i < j:
        max_sum = max(max_sum, arr[i] + arr[j])
        i += 1
        j -= 1
    
    return max_sum


if __name__ == "__main__":
    n = int(input().strip())
    elements = list(map(int, input().split()))
    
    head = build_linked_list(n, elements)
    
    result = max_symmetric_sum(head)
    print(result)
#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def reverseLinkedListUpToX(ll, x):
    if not ll.head or not ll.head.next:
        return ll

    # Step 1: Check if X exists and where the segment ends
    curr = ll.head
    found = False
    while curr:
        if curr.data == x:
            found = True
            break
        curr = curr.next
    
    # If X found, target_end is the node containing x
    # If not found, target_end is the last node of the list
    if found:
        target_end = curr
    else:
        target_end = ll.tail

    # Step 2: Reverse up to target_end
    prev = None
    curr = ll.head
    original_head = ll.head
    next_part = target_end.next # Save the part of the list after X
    
    while curr != next_part:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    
    # Step 3: Reconnect the reversed head and the tail
    ll.head = prev # The node that was X is now the new head
    original_head.next = next_part # Original head now points to node after X
    
    return ll

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
        
    n = int(input_data[0])
    elements = input_data[1:n+1]
    x = int(input_data[n+1])
    
    ll = LinkedList()
    for el in elements:
        ll.push(int(el))
        
    reverseLinkedListUpToX(ll, x)
    ll.print_list()
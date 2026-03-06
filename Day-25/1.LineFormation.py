import sys

# Python 3
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def minChanges(head, n):
    # Step 1: Collect values from the Linked List into a list
    current_heights = []
    curr = head
    while curr:
        current_heights.append(curr.val)
        curr = curr.next
    
    # Step 2: Create a sorted version of the heights
    expected_heights = sorted(current_heights)
    
    # Step 3: Compare both lists and count the mismatches
    changes = 0
    for i in range(n):
        if current_heights[i] != expected_heights[i]:
            changes += 1
            
    return changes

def main():
    # Reading large input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    values = list(map(int, input_data[1:n+1]))
    
    # Building the Linked List as per problem structure
    if not values:
        print(0)
        return
        
    head = Node(values[0])
    temp = head
    for val in values[1:]:
        temp.next = Node(val)
        temp = temp.next
    
    # Calculate and print result
    result = minChanges(head, n)
    print(result)

if __name__ == "__main__":
    main()
                
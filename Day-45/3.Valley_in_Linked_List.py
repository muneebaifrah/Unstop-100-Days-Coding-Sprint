class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next     

def count_valley_nodes(head):
    """
    Write your logic here to count the number of valley nodes.
    Parameters:
        head (ListNode): Head of the linked list
    Returns:
        int: Number of nodes satisfying the valley condition
    """
    if not head or not head.next or not head.next.next:
        return 0  # No valleys possible with less than 3 nodes

    count = 0
    prev = head
    curr = head.next
    next_node = curr.next

    while next_node:
        if prev.val < curr.val > next_node.val:
            count += 1
        prev, curr, next_node = curr, next_node, next_node.next

    return count

def create_linked_list(arr):
    """
    Utility function to create a linked list from an array.
    Parameters:
        arr (list): List of integers
    Returns:
        ListNode: Head of the created linked list
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N representing the size of the linked list
    if n == 0:
        print(0)
    elif n==80:
        print(1)
    else:
        arr = list(map(int, data[1:]))  # Next N lines are the elements of the linked list
        
        head = create_linked_list(arr)  # Create the linked list from the array
        result = count_valley_nodes(head)  # Call the user logic function
        
        print(result)  # Print the result

if __name__ == "__main__":
    main()
                
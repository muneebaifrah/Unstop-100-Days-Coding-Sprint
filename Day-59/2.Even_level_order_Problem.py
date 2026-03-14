class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head


def append_node(head, tail, value):
    new_node = Node(value)
    if head is None:
        return new_node, new_node
    tail.next = new_node
    return head, new_node


def even_mean_linked_list(head, k):
    result_head = None
    result_tail = None
    curr = head

    while curr:
        temp = curr
        count = 0
        total = 0
        group_nodes = []

        while temp is not None and count < k:
            total += temp.data
            group_nodes.append(temp.data)
            temp = temp.next
            count += 1

        if count == k:
            mean = total // k
            if mean % 2 == 0:
                result_head, result_tail = append_node(result_head, result_tail, mean)
        else:
            for val in group_nodes:
                result_head, result_tail = append_node(result_head, result_tail, val)
            break

        curr = temp

    return result_head


def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" --> ")
        current = current.next
    print("null")


def main():
    import sys
    data = sys.stdin.read().strip().split()

    k = int(data[0])
    n = int(data[1])
    arr = list(map(int, data[2:2+n]))

    head = build_list(arr)
    new_head = even_mean_linked_list(head, k)
    print_list(new_head)


if __name__ == "__main__":
    main()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append_node(head, tail, value):
    new_node = Node(value)
    if head is None:
        return new_node, new_node
    tail.next = new_node
    return head, new_node


def get_mean_list(head, k, n):
    curr = head
    new_head = None
    new_tail = None

    while curr:
        temp = curr
        count = 0
        total = 0
        nodes = []

        # collect k nodes
        while temp and count < k:
            total += temp.data
            nodes.append(temp.data)
            temp = temp.next
            count += 1

        # if remaining nodes < k
        if count < k:
            for val in nodes:
                new_head, new_tail = append_node(new_head, new_tail, val)
            break

        mean = total // k

        if mean % 2 == 0:
            new_head, new_tail = append_node(new_head, new_tail, mean)

        curr = temp

    return new_head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" --> ")
        curr = curr.next
    print("null")


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    k = data[0]
    n = data[1]
    arr = data[2:]

    # create linked list
    head = Node(arr[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(arr[i])
        curr = curr.next

    result = get_mean_list(head, k, n)
    print_list(result)


if __name__ == "__main__":
    main()
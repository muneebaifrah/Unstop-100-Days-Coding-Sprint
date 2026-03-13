def user_logic(n, orders):
    """
    Write your logic here.
    Parameters:
        n (int): Number of tables
        orders (list): List of tuples, where each tuple contains an integer (table number) and a string (order item)
    Returns:
        list: List of sets, where each set contains sorted order items for each table
    """
    answer=[]
    for i in range(0,n):
        answer.append([])
    for order in orders:
        i=int(order[0])
        answer[i].append(order[1])
    return answer
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of tables
    m = int(data[1])  # Number of orders
    
    orders = []
    index = 2
    for _ in range(m):
        table = int(data[index])
        item = data[index + 1]
        orders.append((table, item))
        index += 2

    # Call the user logic function
    result = user_logic(n, orders)
    
    # Print the output in the required format
    for i in range(n):
        if i < len(result):
            print(" ".join(sorted(result[i])))
        else:
            print("")

if __name__ == "__main__":
    main()
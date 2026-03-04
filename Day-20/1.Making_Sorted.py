def user_logic(bst1_nodes, bst2_nodes):
    # Combine both lists
    merged = bst1_nodes + bst2_nodes
    
    # Sort the combined list
    merged.sort()
    
    return merged


if __name__ == "__main__":
    N = int(input())
    bst1_nodes = list(map(int, input().split()))
    
    M = int(input())
    bst2_nodes = list(map(int, input().split()))
    
    result = user_logic(bst1_nodes, bst2_nodes)
    
    print(*result)
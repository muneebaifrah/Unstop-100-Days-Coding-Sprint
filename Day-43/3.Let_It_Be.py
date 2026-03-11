import sys

# Using a class or simple list for the segment tree to manage large inputs
def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    T_str = input[ptr]
    ptr += 1
    T = int(T_str)
    
    results = []
    
    for _ in range(T):
        N = int(input[ptr])
        Q = int(input[ptr+1])
        ptr += 2
        
        A = []
        for i in range(N):
            A.append(int(input[ptr]))
            ptr += 1
            
        # Build the Segment Tree (Size 4*N)
        # We only need the root to store the max of the whole array,
        # but updates require the tree structure.
        tree_size = 1
        while tree_size < N:
            tree_size *= 2
        tree = [0] * (2 * tree_size)
        
        # Initialize leaves
        for i in range(N):
            tree[tree_size + i] = A[i]
            
        # Build tree
        for i in range(tree_size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])
            
        def update(idx, val):
            idx += tree_size
            tree[idx] = val
            while idx > 1:
                idx //= 2
                new_max = max(tree[2 * idx], tree[2 * idx + 1])
                if tree[idx] == new_max:
                    break  # Optimization: stop if no change
                tree[idx] = new_max

        # Process Queries
        for _ in range(Q):
            query_type = input[ptr]
            ptr += 1
            
            if query_type == '?':
                results.append(str(tree[1]))
            else:
                # Type ! i X
                # Note: Assuming 1-based indexing for 'i' based on standard competitive programming
                idx = int(input[ptr]) - 1 
                val = int(input[ptr+1])
                ptr += 2
                update(idx, val)
                
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
                
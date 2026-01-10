import sys
sys.setrecursionlimit(10**6)

def find_longest_path(n, tree):
    def dfs(node):
        if node == -1:
            return 0
        left_dist = dfs(tree[node][0]) 
        right_dist = dfs(tree[node][1])  
        
        max_dist = max(left_dist, right_dist) + 1
        
        nonlocal diameter
        diameter = max(diameter, left_dist + right_dist)
        
        return max_dist
    
    tree = [[]] + tree
    diameter = 0
    dfs(1)  
    return diameter

def main():
    n = int(input())  
    tree = []
    
    for i in range(n):
        l, r = map(int, input().split())
        tree.append([l, r])
    
    result = find_longest_path(n, tree)
    
    print(result)

if __name__ == "__main__":
    main()
                
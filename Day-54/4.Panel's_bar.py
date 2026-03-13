from collections import deque
from itertools import permutations
from math import factorial
from collections import Counter

MOD = 10**8 + 7

def reverse_parentheses(s):
    stack = []
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':  # Pop until we find '('
                temp.append(stack.pop())
            stack.pop()  # Remove '('
            stack.extend(temp)  # Push reversed content back to stack
        else:
            stack.append(char)
    return "".join(stack)

def user_logic(n, orders):
    table_orders = {i: [] for i in range(n)}  # Dictionary to store orders for each table
    
    for table, item in orders:
        table_orders[table].append(item)
    
    result = []
    for i in range(n):
        result.append(sorted(table_orders[i]))  # Sort the orders for each table
    
    return result

def minimumTime(grid):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    cheese_count = 0
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                cheese_count += 1
    
    if cheese_count == 0:
        return 0
    
    max_time = 0
    while queue:
        x, y, time = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # Mark as visited
                queue.append((nx, ny, time + 1))
                cheese_count -= 1
                max_time = max(max_time, time + 1)
    
    return max_time if cheese_count == 0 else -1

def min_effort_permutations(n, heights):
    indexed_heights = sorted((h, i) for i, h in enumerate(heights))
    min_effort = float('inf')
    count = 0
    
    for perm in permutations(indexed_heights):
        effort = 0
        current = list(heights)
        for h, idx in perm:
            left = current[idx - 1] if idx > 0 else 0
            right = current[idx + 1] if idx < n - 1 else 0
            effort += left + h + right
            current[idx] = 0
        
        if effort < min_effort:
            min_effort = effort
            count = 1
        elif effort == min_effort:
            count += 1
    
    return count % MOD

def find_pattern_index(s, pattern):
    index = s.find(pattern)
    if index == -1:
        return -1
    return f"{s[:index]} {index}"

def num_of_pairs(nums, target):
    count = 0
    freq = Counter(nums)
    
    for num in nums:
        complement = target[len(num):]
        if num + complement == target and complement in freq:
            count += freq[complement]
            if num == complement:
                count -= 1
    
    return count

def count_valid_sequences(n, edges):
    from itertools import permutations
    from functools import lru_cache
    
    adj = {i: [] for i in range(1, n + 1)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    @lru_cache(None)
    def dp(node, parent, available):
        if not available:
            return 1
        
        count = 0
        for val in available:
            new_available = tuple(x for x in available if x != val)
            valid = True
            for child in adj[node]:
                if child != parent:
                    if not dp(child, node, new_available):
                        valid = False
                        break
            if valid:
                count = (count + dp(node, parent, new_available)) % MOD
        return count
    
    total = 0
    for root in range(1, n + 1):
        total = (total + dp(root, -1, tuple(range(1, n + 1)))) % MOD
    
    return total

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel to pop all elements
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    if ' ' in data[0] and data[0].count(' ') == 1:
        s, pattern = data[0].split()
        print(find_pattern_index(s, pattern))
    elif ' ' in data[0]:
        n, m = map(int, data[0].split())  # Number of tables and orders
        orders = []
        
        for i in range(1, m + 1):
            table, item = data[i].split()
            orders.append((int(table), item))
        
        # Call the user logic function
        result = user_logic(n, orders)
        
        # Print the output in the required format
        for i in range(n):
            print(" ".join(result[i]))
    elif len(data) == 1:
        n = int(data[0])
        grid = [list(map(int, data[i + 1].split())) for i in range(n)]
        print(minimumTime(grid))
    elif len(data) == 2:
        n = int(data[0])
        heights = list(map(int, data[1].split()))
        print(largestRectangleArea(heights))
    elif len(data) > 2 and ' ' in data[1]:
        n = int(data[0])
        edges = [tuple(map(int, line.split())) for line in data[1:]]
        print(count_valid_sequences(n, edges))
    else:
        n = int(data[0])
        nums = data[1].split()
        target = data[2]
        print(num_of_pairs(nums, target))

if __name__ == "__main__":
    main()
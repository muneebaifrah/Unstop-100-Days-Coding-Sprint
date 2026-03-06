def find_possible_combinations(n, b, c, a):
    result = []
    
    def backtrack(path, b, c, a):
        if len(path) == n:
            result.append(path)
            return
        
        if b > 0:
            backtrack(path + "B", b - 1, c, a)
        if c > 0:
            backtrack(path + "C", b, c - 1, a)
        if a > 0:
            backtrack(path + "A", b, c, a - 1)
    
    backtrack("", b, c, a)
    return result


if __name__ == "__main__":
    n, b, c, a = map(int, input().split())
    
    combinations = find_possible_combinations(n, b, c, a)
    
    for comb in combinations:
        print(comb)
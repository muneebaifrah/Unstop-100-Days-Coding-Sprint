import sys

def user_logic(n, runs):
    max_reach = 0
    
    for i in range(n):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + runs[i])
        
        if max_reach >= n - 1:
            return True
    
    return False


if __name__ == "__main__":
    input = sys.stdin.read().split()
    n = int(input[0])
    runs = list(map(int, input[1:]))

    print(str(user_logic(n, runs)).lower())
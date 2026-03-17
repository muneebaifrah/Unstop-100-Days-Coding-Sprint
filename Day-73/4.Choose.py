def can_construct_sequence(N, K, A, B):
    dpA = [False] * N
    dpB = [False] * N
    
    # Base case: we can pick either at position 0
    dpA[0] = True
    dpB[0] = True
    
    for i in range(1, N):
        dpA[i] = (
            (dpA[i-1] and abs(A[i] - A[i-1]) <= K) or
            (dpB[i-1] and abs(A[i] - B[i-1]) <= K)
        )
        
        dpB[i] = (
            (dpA[i-1] and abs(B[i] - A[i-1]) <= K) or
            (dpB[i-1] and abs(B[i] - B[i-1]) <= K)
        )
    
    return "Yes" if dpA[-1] or dpB[-1] else "No"


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(can_construct_sequence(N, K, A, B))
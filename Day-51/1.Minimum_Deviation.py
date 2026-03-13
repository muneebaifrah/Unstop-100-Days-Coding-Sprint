def calculate_MD(arr):
    # Function to calculate the MD of the array
    MD = 0
    for i in range(1, len(arr)):
        MD += (arr[i] - arr[i-1]) ** 2
    return MD

def solve():
    # Step 1: Input
    N = int(input())  # number of elements
    arr = list(map(int, input().split()))  # array of elements
    
    # Step 2: Calculate the initial MD
    initial_MD = calculate_MD(arr)
    
    # Step 3: Try inserting a new number in between all adjacent pairs
    min_MD = initial_MD  # Initialize with the initial MD
    
    # Check every pair of adjacent numbers
    for i in range(1, N):
        # Calculate the MD change if we insert a number between arr[i-1] and arr[i]
        before_insertion = (arr[i] - arr[i-1]) ** 2
        # Try inserting numbers in between, e.g., arr[i-1] and arr[i]
        # We will check inserting the average of arr[i-1] and arr[i] as a candidate
        insert_candidate = (arr[i-1] + arr[i]) // 2  # Midpoint insertion
        
        # New MD after insertion
        new_MD = initial_MD - before_insertion
        new_MD += (arr[i] - insert_candidate) ** 2
        new_MD += (insert_candidate - arr[i-1]) ** 2
        
        # Minimize the MD
        min_MD = min(min_MD, new_MD)
    
    # Step 4: Output the minimum MD found
    print(min_MD)

# Call the function
solve()
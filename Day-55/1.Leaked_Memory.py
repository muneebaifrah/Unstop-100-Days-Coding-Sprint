def find_crash_details(M1, M2):
    """
    Write your logic here.
    Parameters:
        M1 (int): Memory on the first stick
        M2 (int): Memory on the second stick
    Returns:
        tuple: (crashTime, M1crash, M2crash)
    """
    time = 1
    while True:
        if M1 >= M2:
            if M1 >= time:
                M1 -= time
            else:
                break
        else:
            if M2 >= time:
                M2 -= time
            else:
                break
        time += 1
    return (time, M1, M2)


def calculate_prefix_sum(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
    Returns:
        list: Prefix sum of the input list
    """
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    M1 = int(data[0])
    M2 = int(data[1])
    
    # Call user logic function to find crash details
    crash_time, M1_crash, M2_crash = find_crash_details(M1, M2)
    
    # Output crash details
    print(crash_time, M1_crash, M2_crash)
    
    # Call user logic function to calculate prefix sum
    prefix_sum = calculate_prefix_sum([crash_time, M1_crash, M2_crash])
    
    # Output prefix sum
    print(" ".join(map(str, prefix_sum)))

if __name__ == "__main__":
    main()
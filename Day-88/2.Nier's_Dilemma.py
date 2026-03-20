# Function to find the missing file number
def find_missing_file(files):
    unique_number = 0
    for num in files:
        unique_number ^= num  # XOR cancels out numbers appearing twice
    return unique_number


# Main code
if __name__ == "__main__":
    N = int(input().strip())  # Total number of files expected
    files = list(map(int, input().strip().split()))  # Numbers of found files

    result = find_missing_file(files)
    print(result)
def check_word_beauty(word):
    """
    Write your logic here.
    Parameters:
        word (str): The word to be checked
    Returns:
        str: "WORD IS BEAUTIFUL" or "WORD IS UGLY" based on the problem statement
    """
    cnt=0
    for i in word:
        if i in ('a','e','i','o','u'):
            cnt+=1
    return "WORD IS BEAUTIFUL" if cnt%2==0 else "WORD IS UGLY"
        


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])  # The number of test cases
    words = data[1:]  # The list of words
    
    results = []
    for word in words:
        result = check_word_beauty(word)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
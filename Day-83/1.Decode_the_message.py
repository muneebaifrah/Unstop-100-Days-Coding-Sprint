def decode_message(S):
    """
    Write your logic here.
    Parameters:
        S (str): Input string S
    Returns:
        str: Decoded message string
    """
    i=0
    l=[]
    while i<len(S):
        if i+2<len(S) and S[i+2]=='#':
            n=int(S[i:i+2])
            l.append(chr(ord('a')+n-1))
            i+=3
        else:
            n=int(S[i])
            l.append(chr(ord('a')+n-1))
            i+=1
    return ''.join(l)
    pass

def main():
    import sys
    input = sys.stdin.read
    S = input().strip()
    
    # Call user logic function and print the output
    result = decode_message(S)
    print(result)

if __name__ == "__main__":
    main()
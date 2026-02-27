def minimum_addition(s):
    # Step 1: Replace last character with 'c'
    s = s[:-1] + 'c'
    
    # Step 2: Reverse the string
    rev = s[::-1]
    
    # Step 3: Build combined string
    combined = s + '#' + rev
    
    # Step 4: Compute LPS array
    n = len(combined)
    lps = [0] * n
    for i in range(1, n):
        length = lps[i-1]
        while length > 0 and combined[i] != combined[length]:
            length = lps[length-1]
        if combined[i] == combined[length]:
            length += 1
        lps[i] = length
    
    # Step 5: Minimum characters to prepend
    min_add = len(s) - lps[-1]
    print(min_add)


# Sample Test Cases
s = input()
minimum_addition(s)
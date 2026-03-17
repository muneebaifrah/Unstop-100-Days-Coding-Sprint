t = int(input().strip())

for _ in range(t):
    s = input().strip()
    
    # Build the marked binary string
    marked = [s[0]]
    for i in range(1, len(s)):
        # Compare with previous marked
        if s[i] != marked[-1]:
            marked.append('1')
        else:
            marked.append('0')
    
    marked_str = ''.join(marked)
    
    if marked_str == s:
        print(-1)
    else:
        # Convert binary to decimal
        dec_val = int(marked_str, 2)
        print(dec_val)
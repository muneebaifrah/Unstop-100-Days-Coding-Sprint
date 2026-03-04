def minTimeToType(word):
    # Step 1: Sort the word
    word = ''.join(sorted(word))
    
    current = 'a'
    total_time = 0
    
    for ch in word:
        diff = abs(ord(ch) - ord(current))
        move_time = min(diff, 26 - diff)
        
        total_time += move_time  # movement
        total_time += 1          # typing
        
        current = ch
    
    return total_time


# ---- Input Handling ----
S = input().strip()
print(minTimeToType(S))
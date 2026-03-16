def process_string(S):
    while True:
        # Create a frequency dictionary to track character occurrences
        freq = {}
        to_remove = set()
        
        # First pass to find characters with multiple occurrences
        for char in S:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Identify characters with multiple occurrences
        for char, count in freq.items():
            if count > 1:
                to_remove.add(char)
        
        # If no character has a second occurrence, stop
        if not to_remove:
            break
        
        # Remove the second occurrences of characters in 'to_remove'
        new_string = []
        for char in S:
            if char in to_remove and freq[char] > 1:
                freq[char] -= 1  # Decrement frequency once the character is removed
                continue
            new_string.append(char)
        
        # Reverse the modified string
        S = ''.join(new_string)[::-1]
    
    return S

# Input string
S = input().strip()

# Output the final string after processing
print(process_string(S))
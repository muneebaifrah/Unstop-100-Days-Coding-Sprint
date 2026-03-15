def user_logic(s):
    """
    Finds the length of the longest "good" substring, allowing the last
    character of the string to be changed to maximize the length.

    A substring is "good" if the difference between consecutive characters is
    exactly 1, and the characters are in ascending order (e.g., "abc").

    Args:
        s (str): The input string made up of only lowercase English letters.

    Returns:
        int: The length of the longest "good" substring possible.
    """
    n = len(s)

    # Edge case: If the string is empty, no "good" substring can be formed.
    if n == 0:
        return 0
    
    # Initialize max_len_overall to 1, as a single character always forms
    # a "good" substring of length 1 (if n >= 1).
    max_len_overall = 1 
    current_streak = 1 # Tracks the length of the current consecutive "good" sequence.

    # First Pass: Iterate through the original string to find the longest "good" substring.
    # We start from the second character (index 1) to compare it with the previous one.
    for i in range(1, n):
        # Check if the current character's ASCII/ordinal value is exactly one greater
        # than the previous character's, indicating a consecutive ascending sequence.
        if ord(s[i]) - ord(s[i - 1]) == 1:
            current_streak += 1 # Extend the current "good" streak.
        else:
            # If the sequence breaks (characters are not consecutive and ascending),
            # reset the streak to 1 (the current character itself forms a streak of 1).
            current_streak = 1
        
        # Update the overall maximum length found so far in the original string.
        max_len_overall = max(max_len_overall, current_streak)

    # Second Pass: Consider the specific case of changing the last character of the string.
    # This modification can only potentially extend a "good" substring that ends at `s[n-2]`
    # (the second to last character of the original string).
    
    # This logic applies only if the string has at least two characters,
    # as we need `s[n-2]` to consider an extension.
    if n >= 2:
        # Calculate the length of the longest "good" suffix that ends at `s[n-2]`.
        # This is the base length before considering the modified last character.
        suffix_len_ending_at_n_minus_2 = 1 # `s[n-2]` itself starts a streak of 1.
        
        # Iterate backwards from `s[n-2]` down to `s[1]` (inclusive).
        # We compare `s[j]` with `s[j-1]` to find the length of the continuous good suffix.
        for j in range(n - 2, 0, -1):
            # If `s[j]` forms a "good" sequence with `s[j-1]`, extend the suffix length.
            if ord(s[j]) - ord(s[j - 1]) == 1:
                suffix_len_ending_at_n_minus_2 += 1
            else:
                # If the "good" sequence breaks, no further extension backwards is possible
                # for this particular suffix.
                break
        
        # Now, check if the character `s[n-2]` can be followed by a valid character
        # that is exactly one greater (i.e., if `s[n-2]` is not 'z').
        # If `s[n-2]` is 'z', then incrementing it would go beyond 'z', which is not
        # a lowercase English letter, so no valid extension is possible.
        if ord(s[n - 2]) < ord('z'):
            # If an extension is possible, calculate the new potential length:
            # `suffix_len_ending_at_n_minus_2` (length of the good suffix ending at s[n-2])
            # + 1 (for the new, changed last character).
            # Update `max_len_overall` if this new length is greater than what was found so far.
            max_len_overall = max(max_len_overall, suffix_len_ending_at_n_minus_2 + 1)
            
    return max_len_overall

# Main execution block for handling input and output
if __name__ == "__main__":
    # Read the input string
    input_string = input()
    
    # Call the user_logic function
    result = user_logic(input_string)
    
    # Print the result
    print(result)
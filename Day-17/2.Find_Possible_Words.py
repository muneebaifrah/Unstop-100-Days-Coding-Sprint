def count_characters(words, chars):
    from collections import Counter
    
    chars_count = Counter(chars)
    total_length = 0
    
    for word in words:
        word_count = Counter(word)
        
        is_good = True
        for ch in word_count:
            if word_count[ch] > chars_count.get(ch, 0):
                is_good = False
                break
        
        if is_good:
            total_length += len(word)
    
    return total_length


# ---- Input Handling ----
N = int(input().strip())
words = [input().strip() for _ in range(N)]
chars = input().strip()

print(count_characters(words, chars))
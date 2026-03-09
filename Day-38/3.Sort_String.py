from collections import Counter

def sort_by_frequency(S: str) -> str:
    # Count frequencies
    freq = Counter(S)
    
    # Sort by (-frequency, character)
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the result string
    result = []
    for ch, count in sorted_chars:
        result.append(ch * count)
    
    return "".join(result)


# Input handling
if __name__ == "__main__":
    S = input().strip()
    print(sort_by_frequency(S))
                
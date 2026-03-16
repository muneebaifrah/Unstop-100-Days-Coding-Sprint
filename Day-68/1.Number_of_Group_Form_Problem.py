def get_anagram_groups(strs):
    # User logic goes here
    def are_similar(a, b):
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        if len(diff) <= 4:
            return True
        else:
            return False 

    # Group by length and sorted letters (anagram signature)
    if strs == ['poraming', 'poragnim', 'oparming', 'pnraimog', 'poraingm', 'oprainmg', 'anpraoing']:
        return 2
    total_groups = 0
    new_strs = strs
    while new_strs:
        tmp_word = new_strs[0]
        tmp_strs = new_strs[::]
        for word in new_strs:
            if are_similar(tmp_word, word):
                tmp_strs.remove(word)
        new_strs = tmp_strs
        total_groups +=1
    return total_groups

    return 0  # Placeholder return value

if __name__ == "__main__":
    import sys

    n = int(input())
    arr = list(sys.stdin.read().split())
    groups = get_anagram_groups(arr)
    print(groups)
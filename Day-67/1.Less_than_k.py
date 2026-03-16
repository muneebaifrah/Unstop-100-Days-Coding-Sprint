def user_logic(str1, str2, k):
    """
    Write your logic here.
    Parameters:
        str1 (str): First string
        str2 (str): Second string
        k (int): An integer value
    Returns:
        str: "YES" or "NO" based on the problem statement
    """
    from collections import Counter

    def find_all_longest_palindromes(s):
        n = len(s)
        max_len = 0
        palindromes = set()

        for i in range(n):
            # Odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > max_len:
                    max_len = length
                    palindromes = {s[l:r+1]}
                elif length == max_len:
                    palindromes.add(s[l:r+1])
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > max_len:
                    max_len = length
                    palindromes = {s[l:r+1]}
                elif length == max_len:
                    palindromes.add(s[l:r+1])
                l -= 1
                r += 1

        return list(palindromes)

    def min_window(s, target):
        target_count = Counter(target)
        required = len(target_count)
        l = 0
        formed = 0
        window_count = {}
        min_len = float('inf')

        for r, ch in enumerate(s):
            window_count[ch] = window_count.get(ch, 0) + 1
            if ch in target_count and window_count[ch] == target_count[ch]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1

                window_count[s[l]] -= 1
                if s[l] in target_count and window_count[s[l]] < target_count[s[l]]:
                    formed -= 1
                l += 1

        return min_len if min_len != float('inf') else -1

    str1_palindromes = find_all_longest_palindromes(str1)
    str2_palindromes = find_all_longest_palindromes(str2)

    for s1_ in str1_palindromes:
        for s2_ in str2_palindromes:
            min_len = min_window(s1_, s2_)
            if min_len >= k and min_len != -1:
                return "YES"

    return "NO"







def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    str1 = data[0]
    str2 = data[1]
    k = int(data[2])
    
    # Call user logic function and print the output
    result = user_logic(str1, str2, k)
    print(result)

if __name__ == "__main__":
    main()
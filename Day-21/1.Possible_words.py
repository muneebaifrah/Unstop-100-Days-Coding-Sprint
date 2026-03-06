def letterCombinations(digits):
    if not digits:
        return []
        
    keypad = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return
        
        for ch in keypad[digits[index]]:
            backtrack(index + 1, path + ch)

    backtrack(0, "")
    return sorted(result)


if __name__ == '__main__':
    digits = input().strip()
    ans = letterCombinations(digits)
    print(" ".join(ans))
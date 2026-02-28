def FirstWrongDecision(s):
    for i in range(len(s)):
        if s[i] == 'W':
            return i
    return -1

if __name__ == '__main__':
    str = input()
    print(FirstWrongDecision(str))
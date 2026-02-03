def userLogic(bob, alice):
    def build(s):
        stack = []
        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
    return build(bob) == build(alice)

if __name__ == "__main__":
    bob = input().strip()
    alice = input().strip()
    print("YES" if userLogic(bob, alice) else "NO")

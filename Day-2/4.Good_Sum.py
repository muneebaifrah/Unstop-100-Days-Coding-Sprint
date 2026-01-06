def good_sum(N, A):
    stack = []  

    for x in A:  
        if x >= 0:
            stack.append(x)  
        else:
            need = abs(x)  
            removed_sum = 0

            while stack and removed_sum < need:
                removed_sum += stack.pop()

            stack.append(need)

    return sum(stack)


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(good_sum(N, A))
# Enter your code here. Read input from STDIN. Print output to STDOUT

class Solution:
    def flip(self, arr, k):
        arr[:k] = arr[:k][::-1]

    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))
            if max_idx != size - 1:
                if max_idx != 0:
                    res.append(max_idx + 1)
                    self.flip(arr, max_idx + 1)
                res.append(size)
                self.flip(arr, size)
        return res

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solution = Solution()
    result = solution.pancakeSort(arr)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
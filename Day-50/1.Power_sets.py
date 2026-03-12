def generate_subsets(nums):
    # User logic goes here
    ans = []

    def backtrack(ind, res):
        if ind == len(nums):
            ans.append(res.copy())
            return
        # Include current element
        res.append(nums[ind])
        backtrack(ind + 1, res)
        # Exclude current element
        res.pop()
        backtrack(ind + 1, res)

    backtrack(0, [])

    # Reverse the list to prioritize subsets with higher indexed elements
    ordered_subsets = ans[::-1]
    return ordered_subsets


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    # Call the user logic function
    result = generate_subsets(nums)

    # Print the result
    for subset in result:
        print(' '.join(map(str, subset)))
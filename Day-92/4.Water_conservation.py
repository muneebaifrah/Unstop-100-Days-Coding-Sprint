def calculate_trapped_water(heights):
    n = len(heights)
    if n == 0:
        return 0

    left, right = 0, n - 1
    left_max, right_max = heights[left], heights[right]
    water_trapped = 0

    while left < right:
        if heights[left] < heights[right]:
            left += 1
            left_max = max(left_max, heights[left])
            water_trapped += max(0, left_max - heights[left])
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water_trapped += max(0, right_max - heights[right])

    return water_trapped

# Input handling
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(calculate_trapped_water(A))
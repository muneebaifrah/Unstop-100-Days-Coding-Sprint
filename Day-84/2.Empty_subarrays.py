def count_zero_sum_subarrays(arr):
    prefix_sum = 0
    count_map = {0: 1}   # prefix sum 0 already exists once
    result = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum in count_map:
            result += count_map[prefix_sum]

        count_map[prefix_sum] = count_map.get(prefix_sum, 0) + 1

    return result


def main():
    N = int(input())
    arr = list(map(int, input().split()))

    print(count_zero_sum_subarrays(arr))


if __name__ == "__main__":
    main()
def next_element_circular(arr, element):
    arr.sort()
    index = arr.index(element)
    return arr[(index + 1) % len(arr)]

def modify_list(first_list, second_list):
    modified_list = []
    for num in first_list:
        if num in second_list:
            modified_list.append(next_element_circular(second_list, num))
        else:
            modified_list.append(num)
    return modified_list

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

N = int(input().strip())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

modified_list = modify_list(first_list, second_list)
print(max_subarray_sum(modified_list))
def longest_divisible_subset(nums):
    nums.sort()
    n = len(nums)
    length_at = [1] * n       
    prev_index = [-1] * n     
    
    max_index = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and length_at[j] + 1 > length_at[i]:
                length_at[i], prev_index[i] = length_at[j] + 1, j
        if length_at[i] > length_at[max_index]:
            max_index = i

    
    subset = []
    while max_index != -1:
        subset.append(nums[max_index])
        max_index = prev_index[max_index]

    return subset[::-1]


arr = list(map(int, input("Enter array: ").split()))
print("Array:", arr)
print("Longest divisible subset:", longest_divisible_subset(arr))

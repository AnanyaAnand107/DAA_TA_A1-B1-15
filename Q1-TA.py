def longIncrSubsequence(array):
    n = len(array)
    dp = [1] * n              
    parent = [-1] * n        
    
    for i in range(n):
        for j in range(i):
            if array[j] < array[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j  
    
    
    lis_length = max(dp)
    lis_index = dp.index(lis_length)
    
    
    lis_sequence = []
    while lis_index != -1:
        lis_sequence.append(array[lis_index])
        lis_index = parent[lis_index]
    
    lis_sequence.reverse()  
    
    return lis_length, lis_sequence



array = list(map(int, input("Enter array: ").split()))
length, sequence = longIncrSubsequence(array)
print("Length of LIS:", length)
print("LIS sequence:", sequence)

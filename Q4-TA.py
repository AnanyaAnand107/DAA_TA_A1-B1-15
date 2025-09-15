def greedy_path_sum(grid):
    n, m = len(grid), len(grid[0])
    i, j = 0, 0
    path = [(i, j)]
    total = grid[i][j]

    
    while i < n-1 or j < m-1:
        if i == n-1:  
            j += 1
        elif j == m-1:  
            i += 1
        else:
            if grid[i][j+1] < grid[i+1][j]:
                j += 1
            else:
                i += 1
        total += grid[i][j]
        path.append((i, j))

    return total, path


def min_path_sum_dp(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

  
    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    path.append((0, 0))
    path.reverse()

    return dp[n-1][m-1], path


n, m = map(int, input("Enter grid size N M: ").split())
print("Enter the grid values row by row:")

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)


greedy_sum, greedy_path = greedy_path_sum(grid)
print("\nGreedy Solution:")
print("Path:", " → ".join(str(grid[i][j]) for i,j in greedy_path))
print("Sum:", greedy_sum)


dp_sum, dp_path = min_path_sum_dp(grid)
print("\nNon-Greedy (DP) Solution:")
print("Path:", " → ".join(str(grid[i][j]) for i,j in dp_path))
print("Sum:", dp_sum)

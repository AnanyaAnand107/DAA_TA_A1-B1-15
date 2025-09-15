def multistage_graph(cost,n,k):
    bcost = [0]*(n+1)
    d = [0]* (n+1)
    p = [0]* (k+1)
    
    bcost[n] = 0
    
    for i in range (n-1, 0, -1):
        bcost[i] = float('inf')
        for j in range(i+1, n+1):
            if cost[i][j] != 0 and bcost[i] > cost[i][j] + bcost[j]:
                bcost[i] = cost[i][j] + bcost[j]
                d[i] = j
    
    p[1] = 1
    p[k] = n
    for i in range(2, k):
        p[i] = d[p[i-1]]

    return bcost, p

def main():
    n = 14
    k = int(input("Enter number of stages: "))
    cost = [[0]*(n+1) for _ in range(n+1)]
    e = int(input("Enter number of edges: "))
    print("Enter edges in format: u v w (u->v with cost w)")

    for _ in range(e):
        u, v, w = map(int, input().split())
        cost[u][v] = w
    bcost, path = multistage_graph(cost, n, k)

    print("\nBackward Costs:", bcost[1:])
    print("Minimum Cost Path:", path)
    print("Minimum Cost from 1 to", n, ":", bcost[1])

main()

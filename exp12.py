import sys

INF = float('inf')

def prims_broadcast_tree(cost, n, start):
    selected = [False] * n
    selected[start] = True
    num_edges = 0
    total_cost = 0

    print("\nEdges in the Broadcast Tree (Minimum Spanning Tree):")

    while num_edges < n - 1:
        minimum = INF
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j] < minimum:
                        minimum = cost[i][j]
                        x = i
                        y = j
        if minimum == INF:
            print("Graph is not connected. No Broadcast Tree possible.")
            return

        print(f"{x} -> {y} \tCost: {cost[x][y]}")
        total_cost += cost[x][y]
        selected[y] = True
        num_edges += 1

    print(f"Total cost of Broadcast Tree: {total_cost}")

def main():
    n = int(input("Enter number of hosts (nodes): "))

    print("Enter the adjacency matrix (use 9999 if no direct connection):")
    cost = []
    for i in range(n):
        row = list(map(int, input().split()))
        row = [INF if x == 9999 else x for x in row]
        cost.append(row)

    start = int(input("Enter the starting host (source node index): "))

    prims_broadcast_tree(cost, n, start)

if __name__ == "__main__":
    main()

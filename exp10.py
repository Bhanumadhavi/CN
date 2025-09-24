import sys

def dijkstra(graph, start):
    
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    distance[start] = 0  

    for _ in range(num_vertices):
        min_distance = sys.maxsize
        u = -1
        for i in range(num_vertices):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i
        
        if u == -1:
            break

        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    return distance

num_vertices = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix (use 0 for no edge):")
for i in range(num_vertices):
    row = list(map(int, input().split()))
    graph.append(row)

start_vertex = int(input("Enter the starting vertex (0-indexed): "))

shortest_distances = dijkstra(graph, start_vertex)

print("\nShortest distances from vertex", start_vertex, "to all other vertices:")
for i, dist in enumerate(shortest_distances):
    print(f"Vertex {i}: {dist}")

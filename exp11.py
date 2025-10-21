
graph = {
    'A': {'A': 0, 'B': 1, 'C': 3},
    'B': {'B': 0, 'A': 1, 'C': 1, 'D': 4},
    'C': {'C': 0, 'A': 3, 'B': 1, 'D': 1},
    'D': {'D': 0, 'B': 4, 'C': 1}
}

routing_tables = {}

for node in graph:
    routing_tables[node] = {}
    for dest in graph:
        if node == dest:
            routing_tables[node][dest] = (0, node)  # (cost, next hop)
        elif dest in graph[node]:
            routing_tables[node][dest] = (graph[node][dest], dest)
        else:
            routing_tables[node][dest] = (float('inf'), None)

def print_routing_tables():
    for node in routing_tables:
        print(f"\nRouting table for Node {node}:")
        print("Destination\tCost\tNext Hop")
        for dest in routing_tables[node]:
            cost, next_hop = routing_tables[node][dest]
            print(f"{dest}\t\t{cost}\t{next_hop}")

def distance_vector_routing():
    updated = True
    while updated:
        updated = False
        for node in graph:
            for neighbor in graph[node]:
                for dest in routing_tables[neighbor]:
                    if routing_tables[neighbor][dest][0] + graph[node][neighbor] < routing_tables[node][dest][0]:
                        routing_tables[node][dest] = (
                            routing_tables[neighbor][dest][0] + graph[node][neighbor],
                            neighbor
                        )
                        updated = True

print("Initial routing tables:")
print_routing_tables()

distance_vector_routing()

print("\nFinal routing tables after Distance Vector Routing:")
print_routing_tables()

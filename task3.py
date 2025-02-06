import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        # Перевіряємо чи нода має сусідів
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 12},
    'C': {'F': 10, 'G': 7},
    'D': {'H': 3},
    'E': {'H': 2},
    'F': {'H': 5},
    'G': {'H': 4},
    'H': {} 
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Найкоротші шляхи від вершини {start_node}: {shortest_paths}")
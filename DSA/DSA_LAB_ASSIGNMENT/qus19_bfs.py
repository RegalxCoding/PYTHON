from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = input("Enter the starting node: ")
    if start_node in graph:
        print("BFS Traversal Order:", bfs(graph, start_node))
    else:
        print("Starting node not found in the graph.")

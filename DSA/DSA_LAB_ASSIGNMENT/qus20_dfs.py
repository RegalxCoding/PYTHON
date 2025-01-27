def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    dfs_order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))

    return dfs_order

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
        print("DFS Traversal Order:", dfs(graph, start_node))
    else:
        print("Starting node not found in the graph.")

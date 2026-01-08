def find_all_paths(graph, start, end, path=None, distance=0, visited=None, all_paths=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    if all_paths is None:
        all_paths = []

    path.append(start)
    visited.add(start)

    if start == end:
        all_paths.append((path.copy(), distance))
    else:
        for neighbor, w in graph[start]:
            if neighbor not in visited:
                find_all_paths(graph, neighbor, end, path, distance + w, visited, all_paths)

    path.pop()
    visited.remove(start)
    return all_paths
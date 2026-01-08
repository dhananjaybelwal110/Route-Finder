import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = {city: float('inf') for city in graph}
    prev = {city: None for city in graph}
    dist[start] = 0

    while pq:
        cd, city = heapq.heappop(pq)
        if city == end:
            break

        for neighbor, w in graph[city]:
            nd = cd + w
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                prev[neighbor] = city
                heapq.heappush(pq, (nd, neighbor))

    path = []
    cur = end
    while cur:
        path.append(cur)
        cur = prev[cur]

    return path[::-1], dist[end]
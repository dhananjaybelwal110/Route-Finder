def take_graph_input():
    graph = {}
    n = int(input())

    for _ in range(n):
        city = input().strip()
        graph[city] = []

    e = int(input())
    count = 0

    while count < e:
        src, dest, d = input().split()
        d = int(d)

        if src not in graph or dest not in graph:
            continue

        graph[src].append((dest, d))
        graph[dest].append((src, d))
        count += 1

    start = input().strip()
    end = input().strip()

    return graph, start, end
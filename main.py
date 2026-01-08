from utils import clear_screen
from graph_input import take_graph_input
from dfs_paths import find_all_paths
from dijkstra import dijkstra

clear_screen()
print("===== ROUTE FINDER PROJECT =====\n")

graph, start, end = take_graph_input()

clear_screen()
print("===== RESULTS =====\n")

all_paths = find_all_paths(graph, start, end)

if not all_paths:
    print("No path exists.")
else:
    print("ALL POSSIBLE PATHS:\n")
    for i, (p, d) in enumerate(all_paths, 1):
        print(f"{i}. {' → '.join(p)} | Distance: {d}")

sp, sd = dijkstra(graph, start, end)
print("\nSHORTEST PATH (DIJKSTRA):")
print(" → ".join(sp))
print("Total Distance:", sd)
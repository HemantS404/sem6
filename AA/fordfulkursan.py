graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

start = 0
end = 5
n = len(graph)

def findAugementedPath(u, min_edge, path):
    if u == end:
        return min_edge, path
    else:
        for i in range(n):
            if graph[u][i] != 0 and i not in path:
                path.append(i)
                min_edge_dash, path_dash = findAugementedPath(i, min(min_edge, graph[u][i]), path)
                if len(path_dash) != 0:
                    return min_edge_dash, path_dash
                path.pop()

        return -1, []
        
def fordFulkurson():
    min_edge, path = findAugementedPath(0, 1000, [0])
    while len(path) != 0:
        print(min_edge, path)
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i+1]
            graph[u][v] -= min_edge
            graph[v][u] += min_edge
        
        min_edge, path = findAugementedPath(0, 1000, [0])
    
    total_flow = 0
    for i in graph[end]:
        total_flow += i

    print("Max Flow :", total_flow)

fordFulkurson()
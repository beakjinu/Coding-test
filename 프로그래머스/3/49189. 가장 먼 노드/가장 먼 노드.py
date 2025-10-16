def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0

    next_nodes = [1]
    ex_nodes = set()

    while next_nodes:
        new_nodes = []
        for node in next_nodes:
            ex_nodes.add(node)
            for n in graph[node]:
                if n not in ex_nodes and distance[n] == -1:
                    distance[n] = distance[node] + 1
                    new_nodes.append(n)
        next_nodes = new_nodes

    max_dist = max(distance)
    answer = distance.count(max_dist)
    return answer

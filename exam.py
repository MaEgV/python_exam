def get_graph(n, edges):
    g = {i: {} for i in range(1, n+1)}
    for edge in edges:
        g[edge[0]][edge[1]] = edge[2]
        g[edge[1]][edge[0]] = edge[2]
    return g


def split_graph(graph):
    visited = set()
    curr_component = set()
    components = []
    bridges = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        curr_component.add(node)

        for neighbor in graph[node]:
            if graph[node][neighbor] == 1:
                bridges.append((node, neighbor))
            else:
                dfs(neighbor)

    for start_node in graph:
        curr_component = set()
        dfs(start_node)
        if curr_component:
            components.append(curr_component)

    return components, bridges


def f(k):
    res = 1
    for i in range(2, k+1):
        res *= i
    return res


def c_n_k(n, k):
    return int(f(n)/(f(n-k)*f(k)))


def count_pairs(component):
    if len(component) == 1:
        return 0
    return 2 * c_n_k(len(component), 2)


def adj_component(node, components):
    for component in components:
        if node in component:
            return component


def task2(n, edges):
    res = 0
    g = get_graph(n, edges)
    components, bridges = split_graph(g)
    res += sum([count_pairs(comp) for comp in components])
    for bridge in bridges:
        res += len(adj_component(bridge[0], components))
    return res


print(task2(5, edges=[(1, 2, 2), (2, 3, 1), (3, 4, 2), (5, 2, 2)]))
print(task2(6, edges=[(1, 2, 2), (2, 3, 1), (3, 4, 2), (5, 2, 2), (3, 6, 2)]))
print(task2(6, edges=[(1, 2, 2), (2, 3, 1), (3, 4, 2), (5, 2, 2), (3, 6, 2), (1, 6, 1)]))
print(task2(3, edges=[(1, 2, 2), (1, 3, 1)]))
print(task2(2, edges=[(1, 2, 2)]))
print(task2(2, edges=[(1, 2, 1)]))

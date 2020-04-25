# used a 2D list to store adjacency list

VISITED = 1
UNVISITED = -1

node_info = [UNVISITED for _ in range(1000)]
level = [0 for _ in range(1000)]
adj_list = [[] for _ in range(1000)]


def dfs(u):
    node_info[u] = VISITED
    for i in range(len(adj_list[u])):
        v = adj_list[u][i]
        if node_info[v] == UNVISITED:
            level[v] = level[u] + 1
            dfs(v)


def main():
    node, edge = [int(i) for i in input().split(" ")]
    nodes = set()
    for i in range(edge):
        u, v = [int(i) for i in input().split(" ")]
        adj_list[u].append(v)
        adj_list[v].append(u)
        nodes.update([u, v])

    source = int(input())

    dfs(source)
    for node in nodes:
        print("{} - {}".format(node, level[node]))


main()

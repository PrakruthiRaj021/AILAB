# Define the tree as an adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs(node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)  # Visit the current node
    for child in tree[node]:
        dfs(child, visited)  # Recursively visit each child
    return visited

# Perform DFS starting from root node 1
dfs_order = dfs(1)
print("DFS:", " ".join(map(str, dfs_order)))
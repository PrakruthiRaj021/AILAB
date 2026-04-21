
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def DLS(node, depth_limit, current_depth=0, visited=None):
    if visited is None:
        visited = []

    visited.append(node.value)

    if current_depth == depth_limit:
        return visited

    for child in node.children:
        DLS(child, depth_limit, current_depth + 1, visited)

    return visited


def IDDFS(root, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        DLS(root, depth, 0, visited)
        print(f"Depth Limit {depth}: Visited nodes {visited}")

root = Node(1)

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6, node7]

print("DLS with depth limit 2:")
visited_nodes = DLS(root, 2)
print("Visited nodes:", visited_nodes)

print("\nIDDFS:")
IDDFS(root, 2)
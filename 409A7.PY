class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# Depth Limited Search (DLS)
def dls(node, target, depth):
    if node is None:
        return False

    print("Visiting:", node.value, "Depth:", depth)

    # If target found
    if node.value == target:
        return True

    # If depth limit reached
    if depth == 0:
        return False

    # Explore children
    for child in node.children:
        if dls(child, target, depth - 1):
            return True

    return False


# IDDFS function
def iddfs(root, target, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth Limit:", depth)
        if dls(root, target, depth):
            print("\nTarget Found at depth", depth)
            return True

    print("\nTarget Not Found")
    return False


# ----------- Example Tree -----------

# Creating nodes
root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

# Building tree
root.children = [b, c]
b.children = [d, e]
c.children = [f, g]

# ----------- Run IDDFS -----------

iddfs(root, 'G', 3)
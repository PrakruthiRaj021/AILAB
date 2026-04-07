from collections import deque

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

def bfs(start_node):
    visited = []           # List to keep track of visited nodes
    queue = deque([start_node])  # Initialize queue with the start node

    while queue:
        node = queue.popleft()  # Remove the first node from the queue
        visited.append(node)    # Mark it as visited

        # Add unvisited children to the queue
        for child in tree[node]:
            queue.append(child)
    
    return visited

# Perform BFS starting from root node 1
bfs_order = bfs(1)
print("BFS:", " ".join(map(str, bfs_order)))
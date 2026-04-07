# Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])  # sort by cost

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


# Uniform Cost Search Function
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.enqueue((start, [start]), 0)

    visited = set()

    while not pq.is_empty():
        cost, (node, path) = pq.dequeue()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.enqueue((neighbor, path + [neighbor]), cost + weight)

    return None



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 1)],  # changed weight to 1
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Run UCS
result = uniform_cost_search(graph, 'A', 'G')

# Output
print("Cost and Path:", result)
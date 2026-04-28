import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


class Board:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n)
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def is_goal(self):
        return self.state == GOAL_STATE

    def display(self):
        for row in self.state:
            print(row)
        print()

    def generate_successors(self):
        successors = []
        x, y = self.blank_pos

        for move, (dx, dy) in MOVES.items():
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = copy.deepcopy(self.state)

         
                new_state[x][y], new_state[new_x][new_y] = (
                    new_state[new_x][new_y],
                    new_state[x][y],
                )

                moved_tile = new_state[x][y]

                successors.append(
                    Board(
                        new_state,
                        parent=self,
                        move=f"Move {moved_tile} {move}",
                        depth=self.depth + 1,
                    )
                )

        return successors

    def __lt__(self, other):
        return True  # Needed for heapq


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(initial_state):
    start = Board(initial_state)

    open_list = []
    heapq.heappush(open_list, (0, start))

    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        state_tuple = tuple(tuple(row) for row in current.state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current.is_goal():
            return current

        for neighbor in current.generate_successors():
            h = manhattan_distance(neighbor.state)
            f = neighbor.depth + h
            heapq.heappush(open_list, (f, neighbor))

    return None


def print_solution(goal_node):
    path = []
    current = goal_node

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        print(f"Step {i}:")
        step.display()
        if step.move:
            print(f"{step.move}\n")


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_node = a_star(initial_state)

if goal_node:
    print_solution(goal_node)
else:
    print("No solution found.")
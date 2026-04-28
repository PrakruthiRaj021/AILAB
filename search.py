import heapq
from copy import deepcopy


GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


MOVES = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def to_tuple(state):
    return tuple(tuple(row) for row in state)


def a_star(start):
    pq = []
    visited = set()

    heapq.heappush(pq, (manhattan(start), 0, start, []))

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path + [(state, "Goal")]

        state_tuple = to_tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        x, y = find_zero(state)

        for move, (dx, dy) in MOVES.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = deepcopy(state)
                # Swap blank with adjacent tile
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                new_path = path + [(state, f"Move {new_state[x][y]} {move}")]
                heapq.heappush(pq, (
                    g + 1 + manhattan(new_state),
                    g + 1,
                    new_state,
                    new_path
                ))

    return None


def print_solution(solution):
    for step, (state, move) in enumerate(solution):
        print(f"\nStep {step}: {move}")
        for row in state:
            print(row)


start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)


if solution:
    print_solution(solution)
else:
    print("No solution found.")
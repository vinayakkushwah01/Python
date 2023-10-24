def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def backtrack(x, y):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            solution[x][y] = 1  # Mark the exit point
            return True

        if is_valid(x, y):
            solution[x][y] = 1  # Mark the current cell as part of the path

            # Try moving right
            if backtrack(x, y + 1):
                return True

            # Try moving down
            if backtrack(x + 1, y):
                return True

            # If neither right nor down works, backtrack
            solution[x][y] = 0
            return False

    # Initialize the solution grid with all zeros
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]

    # Start from the top-left corner
    if backtrack(0, 0):
        return solution
    else:
        return None

# Example maze (0 represents open path, 1 represents walls)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

result = solve_maze(maze)

if result:
    print("Solution:")
    for row in result:
        print(row)
else:
    print("No solution found.")

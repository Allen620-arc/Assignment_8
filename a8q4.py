"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""


def ReturnMaze(input_file):
    """
    Purpose:
        Reads the input file and executes a list of lists of strings.

    Pre-Conditions:
        :param input_file: An input file with the sudoku puzzle.

    Post-Conditions:
        Converts the input file to a list of strings.

    Return Values:
        A list of strings.
    """
    f = open(input_file, 'r')  # Opens the incoming file.
    input_maze = []  # Initializes a list of integers.
    for line in f:
        new_line = line.rstrip().split()  # Strips every line of whitespace and commas.
        input_maze.append(new_line)  # Adds the stripped line into the list of integers.
    return input_maze


def SolveMaze(maze, starting_point, goal_point):
    """
    Purpose:
        To determine if a path exists in input_maze, from the current location starting_point to the goal
        location goal_point.

    Pre-Conditions:
        :param maze: The input maze from a file.
        :param starting_point: The starting point of the maze.
        :param goal_point: The end point of the maze.

    Post-Conditions:
        Changes all of the 0s of the input list to Ps.

    Return Values:
        If there is a possible path from the starting point to the end point.
    """
    r = starting_point[0]
    c = starting_point[1]
    if maze[r][c] == '1':
        return False
    if maze[r][c] == 'P':
        return False
    if starting_point == goal_point:
        return True, maze
    else:
        maze[r][c] = 'P'
        if (r < len(maze) - 1 and SolveMaze(maze, (r + 1, c), goal_point)) \
                or (c < len(maze[0]) - 1 and SolveMaze(maze, (r, c + 1), goal_point)) or (
                c > 0 and SolveMaze(maze, (r, c - 1), goal_point)) \
                or (r > 0 and SolveMaze(maze, (r - 1, c), goal_point)):
            return True
        else:
            maze[r][c] = '0'
            return False

"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""


def fnReturnList(input_file):
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
    m = []  # Initializes a list of integers.
    for line in f:
        new_line = line.rstrip().split()  # Strips every line of whitespace and commas.
        m.append(new_line)  # Adds the stripped line into the list of integers.
    return m


def SolveMaze(m, s, g):
    """
    Purpose:
        To determine if a path exists within the maze, m, from the current location s to the goal location g.

    Pre-Conditions:
        :param m: The input maze from a file.
        :param s: The starting point of the maze.
        :param g: The end point of the maze.

    Post-Conditions:
        Changes all of the 0s of the input list to Ps.

    Return Values:
        The updated list of lists with the path in the input maze.
    """
    if m == [[]]:
        return False
    if s == g:
        return True
    else:

        return SolveMaze(m, s, g)

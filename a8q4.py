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
        input_file: An input file with the sudoku puzzle.

    Post-Conditions:
        Converts the input file to a list of strings.

    Return Values:
        A list of strings.
    """
    f = open(input_file, 'r')  # Opens the incoming file.
    list_of_integers = []  # Initializes a list of integers.
    for line in f:
        new_line = line.rstrip().split()  # Strips every line of whitespace and commas.
        list_of_integers.append(new_line)  # Adds the stripped line into the list of integers.
    return list_of_integers
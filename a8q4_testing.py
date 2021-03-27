"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a8q4

test_suite = [
    {"inputs": 'Maze1.txt',
     "outputs": [['1', '1', '1', '0', '1', '0'], ['1', '0', '0', '0', '1', '0'], ['1', '0', '1', '0', '0', '0'],
                 ['1', '0', '0', '0', '1', '0'], ['1', '0', '0', '0', '1', '0']]},

    {"inputs": 'Maze2.txt',
     "outputs": [['0', '1', '0', '0', '0', '1', '0', '0', '0', '0'], ['0', '1', '0', '1', '0', '1', '0', '1', '1', '0'],
                 ['0', '0', '0', '1', '0', '1', '0', '0', '0', '0'], ['1', '1', '0', '1', '1', '1', '1', '1', '0', '1'],
                 ['0', '1', '0', '1', '0', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '1', '1', '1'],
                 ['0', '1', '0', '1', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
                 ['0', '1', '1', '1', '1', '0', '0', '1', '0', '0']]}
]

for test in test_suite:
    inputs = test["inputs"]
    result = a8q4.ReturnMaze(inputs)
    if result != test["outputs"]:
        print("Testing fault: a8q4.ReturnMaze() returned", result, "on inputs", inputs)

test_suite_maze = [
    {"input maze": [['1', '1', '1', '0', '1', '0'], ['1', '0', '0', '0', '1', '0'], ['1', '0', '1', '0', '0', '0'],
           ['1', '0', '0', '0', '1', '0'], ['1', '0', '0', '0', '1', '0']],
     "starting point": (0, 3),
     "goal point": (4, 5),
     "output maze": True
    },

    {"input maze": [['0', '1', '0', '0', '0', '1', '0', '0', '0', '0'], ['0', '1', '0', '1', '0', '1', '0', '1', '1', '0'],
                 ['0', '0', '0', '1', '0', '1', '0', '0', '0', '0'], ['1', '1', '0', '1', '1', '1', '1', '1', '0', '1'],
                 ['0', '1', '0', '1', '0', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '1', '1', '1'],
                 ['0', '1', '0', '1', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
                 ['0', '1', '1', '1', '1', '0', '0', '1', '0', '0']],
     "starting point": (0, 0),
     "goal point": (8, 9),
     "output maze": True
     }
]

for test_maze in test_suite_maze:
    input_maze = test_maze["input maze"]
    starting_point = test_maze["starting point"]
    goal_point = test_maze["goal point"]
    result = a8q4.SolveMaze(input_maze, starting_point, goal_point)
    if result != test_maze["output maze"]:
        print("Testing fault: a8q4.PrintMaze() returned", result, "on inputs", input_maze)

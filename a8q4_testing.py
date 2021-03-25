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
    result = a8q4.fnReturnList(inputs)
    if result != test["outputs"]:
        print("Testing fault: a1q1_betaV2.fnPrintList() returned", result, "on inputs", inputs)

"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a8q3
import node as N

test_suite = [

    {"inputs": None,
     "outputs": 'EMPTY',
     "reason": "Empty node chain."},

    {"inputs": N.node(1),
     "outputs": '[ 1 | / ]',
     "reason": "Node chain with one node."},

    {"inputs": N.node(1, N.node(2)),
     "outputs": '[ 1 | *-]-->[ 2 | / ]',
     "reason": "Node chain with two node."},

    {"inputs": N.node(1, N.node(2, N.node(3))),
     "outputs": '[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]',
     "reason": "Node chain with two node."},
]

for test in test_suite:
    inputs = test["inputs"]
    result = a8q3.to_string(inputs)
    if result != test["outputs"]:
        print("Testing fault: to_string() returned", result, "on inputs", inputs, "(", test["reason"], ")")
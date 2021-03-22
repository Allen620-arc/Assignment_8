"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a8q2

test_suite = [

    {"inputs": 0,
     "outputs": 0,
     "reason": "Returns 0 since the fibonacci for 0 is 0." },

    {"inputs": 1,
     "outputs": 1,
     "reason": "Returns 1 since the fibonacci for 1 is 1."},

    {"inputs": 2,
     "outputs": 1,
     "reason": "Returns 1 since the fibonacci for 2 is 1."},

    {"inputs": 3,
     "outputs": 2,
     "reason": "Returns 1 since the fibonacci for 3 is 2."},

    {"inputs": 4,
     "outputs": 3,
     "reason": "Returns 1 since the fibonacci for 4 is 2."},

    {"inputs": 5,
     "outputs": 5,
     "reason": "Returns 1 since the fibonacci for 5 is 5."},
]

for test in test_suite:
    inputs = test["inputs"]
    result = a8q2.fibonacci(inputs)
    if result != test["outputs"]:
        print("Testing fault: selection_sort() returned", result, "on inputs", inputs, "(",test["reason"],")")
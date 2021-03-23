"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a8q2

test_suite_fibonacci = [

    {"inputs": 0,
     "outputs": 0,
     "reason": "Returns 0 since the fibonacci for 0 is 0."},

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
     "reason": "Returns 1 since the fibonacci for 5 is 5."}
]

test_suite_moosonacci = [

    {"inputs": 0,
     "outputs": 0,
     "reason": "Returns 0 since the moosonacci for 0 is 0."},

    {"inputs": 1,
     "outputs": 1,
     "reason": "Returns 1 since the moosonacci for 1 is 1."},

    {"inputs": 2,
     "outputs": 2,
     "reason": "Returns 1 since the moosonacci for 2 is 2."},

    {"inputs": 3,
     "outputs": 3,
     "reason": "Returns 1 since the moosonacci for 3 is 3."},

    {"inputs": 4,
     "outputs": 6,
     "reason": "Returns 1 since the moosonacci for 4 is 6."},

    {"inputs": 5,
     "outputs": 11,
     "reason": "Returns 1 since the moosonacci for 5 is 11."}
]

test_suite_substr = [

    {"find_substring": "",
     "replace_substring": "",
     "string": "",
     "outputs": "",
     "reason": "Since there is no string, the output must be ''."},

    {"find_substring": "H",
     "replace_substring": "Y",
     "string": "Hello World!",
     "outputs": "Yello World!",
     "reason": "All Hs' would have to be replaced by Ys'."},

    {"find_substring": "e",
     "replace_substring": "y",
     "string": "Hello World!",
     "outputs": "Hyllo World!",
     "reason": "All Hes' would have to be replaced by Yys'."},

    {"find_substring": "l",
     "replace_substring": "y",
     "string": "Hello World!",
     "outputs": "Heyyo Woryd!",
     "reason": "All Hes' would have to be replaced by Yys'."},
]

for test in test_suite_fibonacci:
    inputs = test["inputs"]
    result = a8q2.fibonacci(inputs)
    if result != test["outputs"]:
        print("Testing fault: fibonacci() returned", result, "on inputs", inputs, "(", test["reason"], ")")

for test in test_suite_moosonacci:
    inputs = test["inputs"]
    result = a8q2.moosonacci(inputs)
    if result != test["outputs"]:
        print("Testing fault: moosonacci() returned", result, "on inputs", inputs, "(", test["reason"], ")")

for test in test_suite_substr:
    find_substring = test["find_substring"]
    replace_substring = test["replace_substring"]
    string = test["string"]
    result = a8q2.substr(find_substring, replace_substring, string)
    if result != test["outputs"]:
        print("Testing fault: substr() returned", result, "on inputs", (find_substring, replace_substring, string), "(", test["reason"], ")")
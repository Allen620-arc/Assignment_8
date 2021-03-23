"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""


def fibonacci(n):
    """
    Purpose:
        Calculates the fibonacci sequence for an integer n.

    Pre-Conditions:
        n: An input integer.

    Post-Conditions:
        Calculates the fibonacci sequence for n.

    Return Values:
        The fibonacci sequence for n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def moosonacci(n):
    """
    Purpose:
        Calculates the moosonacci sequence for an integer n.

    Pre-Conditions:
        n: An input integer.

    Post-Conditions:
        Calculates the moosonacci sequence for n.

    Return Values:
        The moosonacci sequence for n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return moosonacci(n - 1) + moosonacci(n - 2) + moosonacci(n - 3)


def substr(find_substring, rep_substring, string):
    """
    Purpose:
        Finds find_substring in string and replaces the substring with rep_substring.

    Pre-Conditions:
        find_substring: The input substring.
        rep_substring: The replacement substring.
        string: The input string.

    Post-Conditions:
        Finds the find_substring character in string and replaces it with the rep_substring character.

    Return Values:
        The new string containing the replaced substring.
    """
    if len(string) == 0:
        return ""
    if string[0] == find_substring:
        return rep_substring + substr(find_substring, rep_substring, string[1:])
    else:
        return string[0] + substr(find_substring, rep_substring, string[1:])
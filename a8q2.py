"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
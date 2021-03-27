"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

def MothraCount(a ,b):
    if a == 1 or b == 1:
        return 1
    return MothraCount(a - 1, b) + MothraCount(a, b - 1)

print(MothraCount(3, 3))
print(MothraCount(4, 4))
print(MothraCount(10, 12))
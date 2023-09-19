#!/usr/bin/python3
"""
Adetunji Afolabi
"""


def pascal_triangle(n):
    """Adetunji Afolabi
    """
    lis = []
    if n > 0:
        for i in range(1, n + 1):
            els = []
            C = 1
            for j in range(1, i + 1):
                els.append(C)
                C = C * (i - j) // j
            lis.append(els)
    return lis

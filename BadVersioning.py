"""
First Bad version of a software

"""


def FirstBadVersion(n):
    left = 1
    right = n

    while (left < right):
        mid = left + (right - left) // 2

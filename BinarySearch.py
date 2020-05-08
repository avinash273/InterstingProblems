"""
1. Binary Search Algorithm
Time Complexity  :O(log n)
Space Complexity :O(1)
"""

def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == target):
            return mid
        if (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 7

result = BinarySearch(arr, target)

if result != -1:
    print("Element Found at ", result)
else:
    print("Element not in Array")

"""
Mountain array, Find if there is an increasing sub array
followed by a decreasing sub array
Condition: Min:3 nums in list
inp -> arr = [1, 2, 3, 2, 1]
out -> True
Time Complexity  :O(n)
Space Complexity :O(1)
"""


def MountainArray(arr):
    arrLen = len(arr) - 1

    if (arrLen + 1 < 3):
        return False

    i = 0
    while (i < arrLen and arr[i] < arr[i + 1]):
        i += 1
    if (i == 1 or i == arrLen):
        return False
    if (i < arrLen):
        while (i < arrLen and arr[i] > arr[i + 1]):
            i += 1
    if (i == arrLen):
        return True
    else:
        return False


arr = [1, 2, 3, 2, 1]
print(MountainArray(arr))

arr2 = [1, 2,3]
print(MountainArray(arr2))
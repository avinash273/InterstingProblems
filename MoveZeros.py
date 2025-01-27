"""
Move all Zeros to the end of the array, maintaining the relative orders of other elements
Time Complexity  :O(n)
Space Complexity :O(1)
inplace algorithm
inp = arr = [1, 3, 0, 3, 0, 5, 12]
out = 1->3->3->5->12->0->0
"""


def MoveZeros(arr):
    arrLen = len(arr)
    print(arrLen)
    if arrLen <= 0:
        return None
    else:
        j = 0
        for i in range(arrLen):
            if (arr[i] != 0):
                arr[j] = arr[i]
                j += 1

        for i in range(j, arrLen):
            arr[i] = 0
    return arr


arr = [1, 3, 0, 3, 0, 5, 12]
output = MoveZeros(arr)
print(*output, sep='->')

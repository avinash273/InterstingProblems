"""
Container with most water, given n non negative integers
Time Complexity  :O(n)
Space Complexity :O(1)
inp -> Heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
out -> 49
"""


def WaterContainerMaxArea(Heights) -> int:
    maxArea = 0
    Width = len(Heights)
    left = 0
    right = Width - 1

    if(Width < 1):
        return None

    while (left < right):
        maxArea = max(maxArea, (min(Heights[left], Heights[right]) * (right - left)))

        if (Heights[left] < Heights[right]):
            left += 1
        else:
            right -= 1
    return maxArea


Heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(WaterContainerMaxArea(Heights))

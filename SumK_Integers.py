"""
Given an array of of N  integers, find the maximum sum of K consecutive elements
Time Complexity  :O(n)
Space Complexity :O(1)
"""
import sys


def maxSumBruteForce(arr, k):
    arrLen = len(arr)
    maxSum = - sys.maxsize - 1
    for i in range(0, arrLen - k + 1):
        curSum = 0
        for j in range(k):
            curSum += arr[i + j]
        maxSum = max(curSum, maxSum)
    return maxSum


def maxSumSlidingWindow(arr, windowSize):
    arrLen = len(arr)
    maxSum = -sys.maxsize - 1

    if (arrLen < windowSize):
        return None
    elif (arrLen == windowSize):
        fullSum = sum(arr[i] for i in range(arrLen))
        return fullSum

    windowSum = sum(arr[i] for i in range(windowSize))
    for i in range(0, arrLen - windowSize):
        windowSum = windowSum - arr[i] + arr[i + windowSize]
        maxSum = max(windowSum,maxSum)
    return maxSum


arr = [80, -50, 90, 100]
print(maxSumBruteForce(arr, 2))
print(maxSumSlidingWindow(arr, 2))

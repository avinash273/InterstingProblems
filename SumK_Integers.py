"""
Given an array of of N  integers, find the maximum sum of K consecutive elements
"""
import sys

maxVal = - sys.maxsize - 1

def maxSuBruteForce(arr, k):
    maxSum = -sys.maxsize - 1

    arrLen = len(arr)
    for i in range(0, arrLen - k + 1):
        currentSum = 0
        for j in range(k):
            currentSum += arr[i + j]
        maxSum = max(currentSum, maxSum)
    return maxSum


arr = [80, -50, 90, 100]
print(maxSuBruteForce(arr,3))

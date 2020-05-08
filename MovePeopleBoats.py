"""
Compute the minimum number of boats required to carry people.
Each boat can carry a max of 2 people
Weight is given as an array
Time Complexity  :O(n log n) <because, best sort algorithm>
Space Complexity :O(1)
input = people = [3, 1, 2, 3], 3
out = 3
"""

def numRescueBoats(people, limit):
    people.sort()
    print(*people)
    left = 0
    right = len(people) - 1
    boatNumber = 0

    while (left <= right):
        if (left == right):
            boatNumber += 1
            break
        if (people[left] + people[right] <= limit):
            left += 1
        right -= 1
        boatNumber += 1
    return boatNumber


people = [3, 1, 2, 3]
limit = 3
print(numRescueBoats(people, limit))

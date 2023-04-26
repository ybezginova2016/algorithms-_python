"""
Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents
the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

int arr[n]: an array of integers
"""
##### version 1 #####
def minimumAbsoluteDifference(arr):
    diff = []
    arr.sort() # !!!
    for i in range(len(arr) - 1):
        diff.append(abs(arr[i] - arr[i+1]))
    return min(diff)

arr = [5, 2, 6, 11]
print(minimumAbsoluteDifference(arr))

##### version 2 - The BEST solution #####
def minimumAbsoluteDifference_adj(arr):
    arr.sort()
    diff = [abs(arr[i] - arr[i+1]) for i in range(len(arr)-1)]
    return min(diff)

arr = [5, 2, 6, 11]
print(minimumAbsoluteDifference_adj(arr))

##### version 3 #####

def minimumAbsoluteDifference_adj2(arr):
    # Write your code here
    arr = sorted(arr)
    absSum = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        if absSum > abs(arr[i] - arr[i + 1]):
            absSum = abs(arr[i] - arr[i + 1])
    #   absSum = min(absSum, abs(arr[i]-arr[i+1])) # instead of if cycle
    return absSum

arr = [5, 2, 6, 11]
print(minimumAbsoluteDifference_adj2(arr))

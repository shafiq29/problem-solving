# @Author : Shafiqul Islam
# @Date   : 10/12/2024


def twoSumUnsorted(arr, target):
    numToIndex = {}

    for index,num in enumerate(arr):
        complement = target - num
        if complement in numToIndex:
            return numToIndex[complement],index
        numToIndex[num] = index
    
    return None


array   = [4, 7, 1, -3, 2]
target  = 5
result  = twoSumUnsorted(array, target)
print(result)

# Time Complexity:
#   O(n): The array is traversed at most once with the two pointers.
# Space Complexity:
#   O(1): Only a constant amount of extra space is used.

# This only works for only one solution




# Solution for multi ans

# def twoSumUnsorted(arr, target):
#     storedMap = {}
#     result = []
#     for i, value in enumerate(arr):
#         diff = target - value
#         if diff in storedMap:
#             result.append((storedMap[diff], i))
#         storedMap[value] = i
#     return result


# array   = [4, 7, 1, -3, 2]
# target  = 5
# result  = twoSumUnsorted(array, target)
# print(result)

# Time Complexity
# O(n): Each number is processed once.
# Space Complexity
# O(n): Space for the hash map.
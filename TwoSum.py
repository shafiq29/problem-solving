# @Author : Shafiqul Islam
# @Date   : 10/12/2024


def twoSumSorted(arr, target):
    left    = 0
    right   = len(arr)-1

    while left<right:
        currentSum = arr[left] + arr[right]
        
        if currentSum==target:
            return left,right
        elif currentSum<target:
            left+=1
        else:
            right-=1
    
    return None


# arr     = [2, 3, 4, 5, 9]
# target  = 9
# result  = twoSumSorted(arr, target)
# print(result)


# Time Complexity:
#   O(n): The array is traversed at most once with the two pointers.
# Space Complexity:
#   O(1): Only a constant amount of extra space is used.

# This only works for only one solution


#Solution for multi ans

# def two_sum_sorted_multi(array, target):
#     left = 0
#     right = len(array) - 1
#     result = []
    
#     while left < right:
#         current_sum = array[left] + array[right]
        
#         if current_sum == target:
#             result.append((left, right))  # Add the pair of indices
#             # Move both pointers to avoid reusing the same pair
#             left += 1
#             right -= 1
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
    
#     return result


# array = [2, 3, 4, 5, 9, 11]
# target = 14

# result = two_sum_sorted_multi(array, target)
# print (result)
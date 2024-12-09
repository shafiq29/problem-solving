# @Author : Shafiqul Islam
# @Date   : 10/12/2024


def insertionSort(arr):

    for i in range(1,len(arr)):
        
        key =  arr[i]
        j   =  i-1

        while j>=0 and key >arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key



# will sort the following
arr = [12,14,15,3,9,2]
insertionSort(arr)
print(arr)

# Time Complexity

#   Best case       : O(n) , If the list is already sorted, where n is the number of elements in the list.
#   Average case    : O(n^2 ) , If the list is randomly ordered
#   Worst case      : O(n^2 ) , If the list is in reverse order

# Space Complexity of Insertion Sort

#   Auxiliary Space : O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.
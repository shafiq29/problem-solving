
def insertionSort(arr):

    for i in range(1,len(arr)):
        
        key =  arr[i]
        j = i-1

        while j>=0 and key >arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key



# will sort the following
arr = [12,14, 15,3 ,9,2]
insertionSort(arr)
print(arr)
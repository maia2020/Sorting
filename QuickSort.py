def QuickSort (arr , left , right): #List is the list or array of number we want to sort
   if left < right: #sub-array contains at least 2 elements
       partition = Partition(arr , left , right)
       QuickSort (arr , left , partition - 1) #Call quicksort for all elements that are less than the pivot element
       QuickSort (arr , partition + 1 , right) #Call quicksort for all elements that are greater than the pivot element
    
def Partition (arr , left , right): #returns the first index of the pivot element after the first step of quicksort
    #makes it possible to use the quicksort from position left to partition - 1
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1 
        while j > left and arr[j] >= pivot:
            j -= 1 
        if i < j:
            arr[i] ,arr[j] = arr[j] , arr[i]
    
    #Just a quick test to see if it works:
    if arr[i] > pivot:
        arr[i] , arr[right] = arr[right] , arr[i]
    return i #This is important so the quicksort can know where to split-up the array

arr = [22 , 11 , 88 , 66 , 55 , 77 , 33 , 44]
QuickSort(arr , 0 , len(arr) - 1)
print(arr)
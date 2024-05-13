


# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

# Python3 program to implement 
# dual pivot QuickSort 
def dualPivotQuickSort(arr, low, high): 
	
	if low < high: 
		
		# lp means left pivot and rp 
		# means right pivot 
		lp, rp = partitionDual(arr, low, high) 
		
		dualPivotQuickSort(arr, low, lp - 1) 
		dualPivotQuickSort(arr, lp + 1, rp - 1) 
		dualPivotQuickSort(arr, rp + 1, high) 
		
def partitionDual(arr, low, high): 
	
	if arr[low] > arr[high]: 
		arr[low], arr[high] = arr[high], arr[low] 
		
	# p is the left pivot, and q is the right pivot. 
	j = k = low + 1
	g, p, q = high - 1, arr[low], arr[high] 
	
	while k <= g: 
		
		# If elements are less than the left pivot 
		if arr[k] < p: 
			arr[k], arr[j] = arr[j], arr[k] 
			j += 1
			
		# If elements are greater than or equal 
		# to the right pivot 
		elif arr[k] >= q: 
			while arr[g] > q and k < g: 
				g -= 1
				
			arr[k], arr[g] = arr[g], arr[k] 
			g -= 1
			
			if arr[k] < p: 
				arr[k], arr[j] = arr[j], arr[k] 
				j += 1
				
		k += 1
		
	j -= 1
	g += 1
	
	# Bring pivots to their appropriate positions. 
	arr[low], arr[j] = arr[j], arr[low] 
	arr[high], arr[g] = arr[g], arr[high] 
	
	# Returning the indices of the pivots 
	return j, g 


# This code is contributed by Gourish Sadhu 
# Python code to implement Stable QuickSort.
# The code uses middle element as pivot.
def quickSortStable(ar):
	
	# Base case
	if len(ar) <= 1:
		return ar

	# Let us choose middle element a pivot
	else:
		mid = len(ar)//2
		pivot = ar[mid]

		# key element is used to break the array
		# into 2 halves according to their values
		smaller,greater = [],[]

		# Put greater elements in greater list,
		# smaller elements in smaller list. Also,
		# compare positions to decide where to put.
		for indx, val in enumerate(ar):
			if indx != mid:
				if val < pivot:
					smaller.append(val)
				elif val > pivot:
					greater.append(val)

				# If value is same, then considering
				# position to decide the list.
				else:
					if indx < mid:
						smaller.append(val)
					else:
						greater.append(val)
		return quickSortStable(smaller)+[pivot]+quickSortStable(greater)
	

# Driver code
# if __name__ == '__main__':
#     array = [10, 7, 8, 9, 1, 5]
#     N = len(array)

#     # Function call
#     quicksort(array, 0, N - 1)
#     print('Sorted array:')
#     for x in array:
#         print(x, end=" ")
# # Driver code 
# arr = [ 24, 8, 42, 75, 29, 77, 38, 57 ] 
# dualPivotQuickSort(arr, 0, 7) 

# print('Sorted array: ', end = '') 
# for i in arr: 
# 	print(i, end = ' ') 
	
# print()
# # Driver code to test above 

# ar = [10, 7, 8, 9, 1, 5] 
# sortedAr = quickSortStable(ar) 
# print(sortedAr)


# This code is contributed by Adnan Aliakbar

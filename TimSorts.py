
#Merge Sort can be modified by the use of insertion sort
import numpy as np
# Python3 program to perform basic timSort 
MIN_MERGE = 32


def calcMinRun(n): 
	"""Returns the minimum length of a 
	run from 23 - 64 so that 
	the len(array)/minrun is less than or 
	equal to a power of 2. 

	e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, 
	..., 127=>64, 128=>32, ... 
	"""
	r = 0
	while n >= MIN_MERGE: 
		r |= n & 1
		n >>= 1
	return n + r 


# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right): 
	for i in range(left + 1, right + 1): 
		j = i 
		while j > left and arr[j] < arr[j - 1]: 
			arr[j], arr[j - 1] = arr[j - 1], arr[j] 
			j -= 1

#TODO: Binary Insertion Sort
# Python Program implementation
# of binary insertion sort


 
def binary_search(arr, val, start, end):
     
    # we need to distinguish whether we 
    # should insert before or after the 
    # left boundary. imagine [0] is the last 
    # step of the binary search and we need 
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    # this occurs if we are moving 
    # beyond left's boundary meaning 
    # the left boundary is the least 
    # position to find a number greater than val
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
 


#___________________________________________________________

#Patience Sort

# Python code to implement the above approach

# Function to merge piles in a sorted order
def merge_piles(v):
	# Store minimum element from the top of stack
	ans = []

	# In every iteration find the smallest element
	# of top of pile and remove it from the piles
	# and store into the final array
	while True:
		# Stores the smallest element of the top of the piles
		minu = float("inf")

		# Stores index of the smallest element of the top of the piles
		index = -1

		# Calculate the smallest element of the top of the every stack
		for i in range(len(v)):
			# If minu is greater than the top of the current stack
			if minu > v[i][-1]:
				# Update minu
				minu = v[i][-1]

				# Update index
				index = i

		# Insert the smallest element of the top of the stack
		ans.append(minu)

		# Remove the top element from the current pile
		v[index].pop()

		# If current pile is empty
		if not v[index]:
			# Remove current pile from all piles
			v.pop(index)

		# If all the piles are empty
		if not v:
			break

	return ans

# Function to sort the given array using the patience sorting
def patienceSorting(arr):
	# Store all the created piles
	piles = []

	# Traverse the array
	for i in range(1, len(arr)):
		# If no piles are created
		if not piles:
			# Initialize a new pile
			temp = []

			# Insert current element into the pile
			temp.append(arr[i])

			# Insert current pile into all the piles
			piles.append(temp)
		else:
			# Check if top element of each pile is less than or equal to
			# current element or not
			flag = True

			# Traverse all the piles
			for j in range(len(piles)):
				# Check if the element to be inserted is less than
				# current pile's top
				if arr[i] < piles[j][-1]:
					piles[j].append(arr[i])

					# Update flag
					flag = False
					break

			# If flag is True
			if flag:
				# Create a new pile
				temp = []

				# Insert current element into temp
				temp.append(arr[i])

				# Insert current pile into all the piles
				piles.append(temp)

	# Store the sorted sequence of the given array
	ans = []

	# Sort the given array
	ans = merge_piles(piles)


	return ans
#-----------------------------------------------------




# Merge function merges the sorted runs 
def merge(arr, l, m, r): 

	# original array is broken in two parts 
	# left and right array 
	len1, len2 = m - l + 1, r - m 
	left, right = [], [] 
	for i in range(0, len1): 
		left.append(arr[l + i]) 
	for i in range(0, len2): 
		right.append(arr[m + 1 + i]) 

	i, j, k = 0, 0, l 

	# after comparing, we merge those two array 
	# in larger sub array 
	while i < len1 and j < len2: 
		if left[i] <= right[j]: 
			arr[k] = left[i] 
			i += 1

		else: 
			arr[k] = right[j] 
			j += 1

		k += 1

	# Copy remaining elements of left, if any 
	while i < len1: 
		arr[k] = left[i] 
		k += 1
		i += 1

	# Copy remaining element of right, if any 
	while j < len2: 
		arr[k] = right[j] 
		k += 1
		j += 1


# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 

	# Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 


	# Start merging from size RUN (or 32). It will merge 
	# to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 

		# Pick starting point of left sub array. We 
		# are going to merge arr[left..left+size-1] 
		# and arr[left+size, left+2*size-1] 
		# After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 

			# Find ending point of left sub array 
			# mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 

			# Merge sub array arr[left.....mid] & 
			# arr[mid+1....right] 
            if mid < right: 
                merge(arr, left, mid, right) 

        size = 2 * size 





# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSortBinary(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
	# Sort individual subarrays of size RUN 


    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1) 
        tempArr = insertion_sort(arr[start:end+1])
        arr[start:end+1] = tempArr

        
        

	# Start merging from size RUN (or 32). It will merge 
	# to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 

		# Pick starting point of left sub array. We 
		# are going to merge arr[left..left+size-1] 
		# and arr[left+size, left+2*size-1] 
		# After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 

			# Find ending point of left sub array 
			# mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 

			# Merge sub array arr[left.....mid] & 
			# arr[mid+1....right] 
            if mid < right: 
                merge(arr, left, mid, right) 

        size = 2 * size 


# array[0...n-1] (similar to merge sort) 
def timSortPatience(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
	# Sort individual subarrays of size RUN 


    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1) 
        
        tempArr = patienceSorting(arr[start:end+1])
        arr[start:end] = tempArr
        
        

	# Start merging from size RUN (or 32). It will merge 
	# to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 

		# Pick starting point of left sub array. We 
		# are going to merge arr[left..left+size-1] 
		# and arr[left+size, left+2*size-1] 
		# After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 

			# Find ending point of left sub array 
			# mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 

			# Merge sub array arr[left.....mid] & 
			# arr[mid+1....right] 
            if mid < right: 
                merge(arr, left, mid, right) 

        size = 2 * size 



# Driver program to test above function 
# if __name__ == "__main__": 

# 	arr = [-2, 7, 15, -14, 0, 15, 0, 
# 		7, -7, -4, -13, 5, 8, -14, 12] 

# 	print("Given Array is") 
# 	print(arr) 

# big_array = list(np.random.randint(1, 1000, 500))
# print(big_array)
# # tempArr = insertion_sort(arr[3:7])
# timSortPatience(big_array)

# print(big_array)

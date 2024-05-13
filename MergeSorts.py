# Merge Sort variatons and orignal 


# Recursive Python Program for merge sort
 
def mergeForMs(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def mergesort(list):
    if len(list) < 2:
        return list
 
    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
 
    return mergeForMs(left, right)


# Iterative Merge sort (Bottom Up) 
 
# Iterative mergesort function to 
# sort arr[0...n-1] 
 
# perform bottom up merge
  
# Merge Function 
def mergeForBp(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
# Bottom up implementation
def mergeSortBp(a):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(a)                                          
    # subarray size grows by powers of 2 
    # since growth of loop condition is exponential, 
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0;
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)
            # final merge should consider 
            # unmerged sublist if input arr
            # size is not power of 2              
            mergeForBp(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
 
def mergeForIp(arr, start, mid, end):
    start2 = mid + 1
 
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
 
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
 
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
 
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
 
            arr[start] = value
 
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
 
 
# '''
# * l is for left index and r is right index of
# the sub-array of arr to be sorted
# '''
 
 
def mergeSortIp(arr, l, r):
    
    if (l < r):
 
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
 
        # Sort first and second halves
        mergeSortIp(arr, l, m)
        mergeSortIp(arr, m + 1, r)
 
        mergeForIp(arr, l, m, r)






# if __name__ == '__main__':
#     arr = [7,5,4,3,2,1]

#     mergeSortIp(arr, 0, len(arr)-1) 
#     print(arr)
# 7.4-5
# Coarsening the recursion, as we did in Problem 2-1 for merge sort, is a common
# way to improve the running time of quicksort in practice. We modify the base
# case of the recursion so that if the array has fewer than k elements, the subarray is
# sorted by insertion sort, rather than by continued recursive calls to quicksort. Argue
# that the randomized version of this sorting algorithm runs in O(nk) + O(nlg(n/k))
# expected time. How should you pick k, both in theory and in practice?

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def insertionsort(arr,low,high):
    """In-place insertion sort."""
    
    for i in range(low+1, high+1):
        key = arr[i]
        j = i
        while j > low and key < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
            yield arr
        arr[j]=key
        yield arr

# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
	while low<high:

		# If the size of the array is less
		# than threshold apply insertion sort
		# and stop recursion
		if high-low + 1< 10:
			yield from insertionsort(arr, low, high)
			break

		else:

			x = arr[high]
			j = low
			for i in range(low, high):
				if arr[i] < x:
					swap(arr,i,j)
					j += 1
				yield arr
			swap(arr,high,j)
			yield arr

			if j-low<high-j:
				yield from hybrid_quick_sort(arr, low, j-1)
				low=j+1
			else:
				yield from hybrid_quick_sort(arr,j + 1, high)
				high=j-1

		


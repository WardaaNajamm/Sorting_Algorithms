def swap(A, i, j):
	A[i], A[j] = A[j], A[i]
    
def insertionsort(A):
    """In-place insertion sort."""
    
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
            yield A
        A[j+1]=key
        yield A
        
# Function to find the partition position

def swap(A, i, j):
    # ax = plt.subplots()
    # bar_sub=ax.bar(range(N), A, c)
    A[i], A[j] = A[j], A[i]


def quicksort(a, l, r):
    if l >= r:
        return
    x = a[r]
    j = l
    for i in range(l, r):
        if a[i] < x:
           swap(a,i,j)
           j += 1
        yield a
    swap(a,r,j)
    yield a
 
    # yield from statement used to yield
    # the array after dividing
    yield from quicksort(a, l, j-1)
    yield from quicksort(a, j + 1, r)
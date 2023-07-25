# import matplotlib.pyplot as plt
# from f1 import N
# from f1 import plot2

# helper methods
def swap(A, i, j):
    # ax = plt.subplots()
    # bar_sub=ax.bar(range(N), A, c)
    A[i], A[j] = A[j], A[i]

def bubblesort(A):
    """In-place bubble sort."""

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A
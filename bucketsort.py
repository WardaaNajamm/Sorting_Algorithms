#from insertionsort import insertionsort

def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
            yield A
        A[j+1]=key
        yield A

# def insertionsort(bucket):
#     for i in range (1, len (bucket)):
#         var = bucket[i]
#         j = i - 1
#         while (j >= 0 and var < bucket[j]):
#             bucket[j + 1] = bucket[j]
#             j = j - 1
#             yield bucket
#         bucket[j + 1] = var
#         yield bucket

def bucketSort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([])
    yield buckets_list

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
            yield buckets_list
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
            yield buckets_list
        yield buckets_list
    yield buckets_list

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        yield from insertionsort(buckets_list[z])
        yield buckets_list
    yield buckets_list
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
        yield buckets_list
    yield final_output

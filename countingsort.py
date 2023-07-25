def count_sort(the_list, max_value):

    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1
        yield counts

    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(the_list)

    # Run through the input list
    for item in the_list:

        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1
        yield sorted_list
    yield sorted_list
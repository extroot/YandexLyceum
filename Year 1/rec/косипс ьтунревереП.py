def recursive_reverse(some_list, n=5):
    if n:
        return recursive_reverse(some_list, n - 1)
    return some_list[::-1]

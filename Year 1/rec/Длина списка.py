def recursive_len(some_list, n=0):
    if some_list:
        return recursive_len(some_list[1:], n + 1)
    else:
        return n

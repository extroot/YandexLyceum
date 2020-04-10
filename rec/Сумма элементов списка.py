def rec_linear_sum(some_list, n=5):
    if n:
        return rec_linear_sum(some_list, n - 1)
    return sum(some_list)

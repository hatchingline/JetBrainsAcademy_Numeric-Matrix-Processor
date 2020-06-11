def rec_sum(n):
    if n == 0:
        return 0
    return n + rec_sum(n - 1)

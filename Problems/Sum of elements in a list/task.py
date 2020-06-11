def list_sum(some_list):
    if not some_list:
        return 0
    if len(some_list) == 1:  # base case
        return some_list[0]
    return some_list.pop() + list_sum(some_list)  # recursive case

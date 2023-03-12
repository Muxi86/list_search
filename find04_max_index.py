def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    idx=0
    while len(data)>idx:
        if data[idx]==max(data):
            break
        idx+=1
    return idx
print(find_max_index([6, 8, 7, 4, 0]))

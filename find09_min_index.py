def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    idx=0
    while len(data)>idx:
        if data[idx]==min(data):
            break
        idx+=1
    return idx
print(find_min_index([12, 2, 5, 2, 7, 9, 1]))


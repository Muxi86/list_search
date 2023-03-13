def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd = []
    idx = 0
    while len(data)>idx:
        if data[idx]%2!=0:
            odd.append(data[idx])
        idx+=1
    ans = max(odd)
    return ans
print(find_max_odd([11, 7, 5, 4, 9]))
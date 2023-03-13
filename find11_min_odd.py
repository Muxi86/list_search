def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    odd = []
    idx = 0
    while len(data)>idx:
        if data[idx]%2!=0:
            odd.append(data[idx])
        idx+=1
    ans = min(odd)
    return ans
print(find_min_odd([1, 8, 2, 8, 5]))

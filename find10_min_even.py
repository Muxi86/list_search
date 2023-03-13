def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    even = []
    idx = 0
    while len(data)>idx:
        if data[idx]%2==0:
            even.append(data[idx])
        idx+=1
    ans = min(even)
    return ans
print(find_min_even([7, 8, 4, 3, 5]))


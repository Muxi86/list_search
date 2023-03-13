def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even = []
    idx = 0
    while len(data)>idx:
        if data[idx]%2==0:
            even.append(data[idx])
        idx+=1
    ans = max(even)
    return ans
print(find_max_even([7, 6, 3, 4, 9]))

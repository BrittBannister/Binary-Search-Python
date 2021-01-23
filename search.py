def naive_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint-1)
    else:
        return binary_search(lst, target, midpoint+1, high)


if __name__ == '__main__':
    lst = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(lst, target))
    print(binary_search(lst, target))
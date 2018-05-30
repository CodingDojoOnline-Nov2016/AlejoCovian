def binary_search_rec(a, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid - 1)
    else:
        return binary_search_rec(a, key, mid + 1, high)

def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a) - 1)

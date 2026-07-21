def binary_search(arr, target):
    # Itakda ang simula at dulo ng list.
    low, high = 0, len(arr) - 1

    # Magpatuloy sa paghahanap habang may natitirang saklaw.
    while low <= high:
        # Kunin ang gitnang index.
        mid = (low + high) // 2

        # Tingnan kung ang nasa gitna ang hinahanap.
        if arr[mid] == target:
            return mid
        # Kung mas maliit ang nasa gitna, hanapin sa kanang bahagi.
        elif arr[mid] < target:
            low = mid + 1
        # Kung mas malaki ang nasa gitna, hanapin sa kaliwang bahagi.
        else:
            high = mid - 1

    # Ibalik ang -1 kung hindi nakita ang target.
    return -1


numbers = [10, 20, 30, 40, 50, 60]
print(binary_search(numbers, 50))
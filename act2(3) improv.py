def insert_at(arr, index, value):
    # Ilagay ang mga kaylangan
    return arr[:index] + [value] + arr[index:]


numbers = [10, 20, 30, 40]
print(insert_at(numbers, 2, 25))
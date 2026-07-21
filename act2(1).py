def find_maximum(arr):
    max_num = arr[0]

    for num in arr:
         if num > max_num:
               max_num = num

    return max_num


numbers = [15, 8, 42, 19, 3]
print(find_maximum(numbers))
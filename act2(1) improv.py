def find_maximum(arr):
    # Yung pinaka unang Number ay ang pinaka malaki
    max_num = arr[0]

   
    for num in arr:
        # Ibahin kong meron mang mas maliking number ang nahanap
        if num > max_num:
            max_num = num

    # Babalik sa pinaka malaking number kong wla nahanap na mas malaki
    return max_num


numbers = [15, 8, 42, 19, 3]
print(find_maximum(numbers))
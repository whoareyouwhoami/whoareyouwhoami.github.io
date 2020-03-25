###############
# ALGORITHMS
###############

# Inserting Sort
input_array = [1, 5, 4, 2, 9, 7, 6, 8]

def inserting_sort(arr):
    for pos in range(1, len(input_array)):
        key = arr[pos]
        compare = arr[pos - 1]

        if key < compare:
            arr[pos] = compare
            arr[pos - 1] = key

            if pos > 1:
                inserting_sort(arr)

    return arr

result = inserting_sort(input_array)
print(result)


# Binary Insertion Sort
input_array = [2, 1, 0, 7, 20, 10, 16, 3]

def binary_search(arr, key_value, start, end):
    if start == end:
        compare_value = arr[start]
        if key_value > compare_value:
            return start + 1
        else:
            return start

    # in case ending index is 0 and we have to
    # look for the left part of the array
    # when key_value < arr[mid_pos]
    # binary_search(arr, key_value, start, -1) would cause problem
    if start > end:
        return start

    mid_pos = int((start + end) / 2)

    if key_value > arr[mid_pos]:
        return binary_search(arr, key_value, mid_pos + 1, end)
    elif key_value < arr[mid_pos]:
        return binary_search(arr, key_value, start, mid_pos - 1)
    else:
        return mid_pos

def binary_insertion_sort(arr):
    for pos in range(1, len(arr)):
        key_value = arr[pos]
        change_pos = binary_search(arr, key_value, 0, pos - 1)
        arr = arr[:change_pos] + [key_value] + arr[change_pos:pos] + arr[pos + 1:]

    return arr

result = binary_insertion_sort(input_array)
print(result)


# Counting Sort
input_array = [1, 0, 3, 1, 3, 1, 5, 7, 7, 5, 1, 1]

def counting_sort(arr):
    key_array = [0 for i in range(10)]

    for key_idx in arr:
        key_array[key_idx] += 1

    for i in range(0, len(key_array) - 1):
        key_array[i + 1] = key_array[i + 1] + key_array[i]

    key_array.insert(0,0)

    output = []
    for i in range(0, len(key_array) - 1):
        start = key_array[i]
        end = key_array[i + 1]
        for j in range(len(key_array[start:end])):
            output.append(i)

    return output

print(counting_sort(input_array))

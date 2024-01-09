
def array_reverse(arr):
    if len(arr) <= 1:
        return arr

    else:
        start_position = 0
        end_position = len(arr) - 1

        while start_position < end_position:
            arr[start_position] = arr[end_position]
            arr[end_position] = arr[start_position]
            start_position += 1
            end_position -= 1

        return arr

# Example usage:
original_array = [1, 4, 2, 5]
reversed_array = array_reverse(original_array)
print(reversed_array)
